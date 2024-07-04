import math
from stairsres.model.networks import EgoWorkNet, EgoPerformanceNet


class ResTimeModel:
    def __init__(self, dbwrapper):
        self.wrapper = dbwrapper

    def get_resources_volumes(self, work_name, work_volume, measurement, shift=11.) -> dict:
        bn_params = self.wrapper.get_res_model(name=work_name, measurement_type=measurement)
        bn = EgoWorkNet()
        if not bn_params:
            print("Database returns None object.")
            return None
        bn.load(bn_params)
        res = bn.leaves
        worker_reqs = {}
        worker_reqs['worker_reqs'] = []
        for r in res:
            params, _ = bn.get_dist(r, {bn.root: work_volume})
            if len(params) > 1:
                _, numbers, hours = params[0], params[1], params[2]
                worker_reqs['worker_reqs'].append({'kind': r,
                                                   'volume': 3*math.ceil(numbers/hours),
                                                   'min_count': math.ceil(numbers/hours),
                                                   'max_count': 5*math.ceil(numbers/hours)})
            else:
                worker_reqs['worker_reqs'].append({'kind': r,
                                                   'volume': 3 * math.ceil(params[0] / shift),
                                                   'min_count': math.ceil(params[0] / shift),
                                                   'max_count': 5 * math.ceil(params[0] / shift)})
        return worker_reqs

    def get_time(self, work_volume: dict, resources: dict, quantile: str, measurement: str) -> float:
        q = 0.5
        if quantile == '0.9':
            q = 0.1
        if quantile == '0.1':
            q = 0.9
        work_name = next(iter(work_volume))
        bn_params = self.wrapper.get_perf_model(name=work_name, measurement_type=measurement)
        model_work_name, model_res_names = next((k[1], [r[0] for r in bn_params['edges']]) for k in bn_params['edges'])
        bn = EgoPerformanceNet()
        bn.load(bn_params)
        test_data = {res_bn_name: resources[res_name] for res_bn_name in model_res_names for res_name in resources if res_name in res_bn_name}
        mu, var = bn.get_dist(model_work_name, test_data)
        return math.ceil(work_volume[work_name] / mu[0])#max(math.ceil(work_volume[work_name] / mu), 1)

    def estimate_time(self, work_unit, worker_list, measurement, mode='0.5'):
        if not worker_list:
            return 0
        if work_unit['volume'] == 0:
            return 0
        work_name = work_unit['name']
        work_volume = work_unit['volume']
        res_dict = {req['name']: req['_count'] for req in worker_list}
        return self.get_time(work_volume={work_name: work_volume}, resources=res_dict, measurement=measurement, quantile=mode) 
