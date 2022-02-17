import os


def is_exist_fun(name, fan_name):
    if not os.path.exists(f'./test/{name}/{fan_name}'):
        os.makedirs(f'./test/{name}/{fan_name}')