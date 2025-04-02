import pickle
from utils import get_Car_models

dic = {}
def get_view_stats():
    from aiogram_run import redis_client
    try:
        view_data = redis_client.get('view_stats')
        view_data_dict = pickle.loads(view_data)
    except:
        return {}
    return view_data_dict

def get_req_stats():
    from aiogram_run import redis_client
    try:
        req_data = redis_client.get('req_stats')
        req_data_dict = pickle.loads(req_data)
    except:
        return {}
    return req_data_dict

# print(get_view_stats())
# print(get_req_stats())

def get_Final_stats():
    view_count = get_view_stats()
    req_count = get_req_stats()

    if not view_count:
        view_count = get_Car_models.Get_Car_models()

    if not req_count:
        req_count = get_Car_models.Get_Car_models()

    for key in view_count:
        dic[key] = [view_count[key], req_count[key]]
    print(view_count)
    print(req_count)

    print(dic)

get_Final_stats()