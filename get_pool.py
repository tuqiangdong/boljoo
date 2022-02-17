import proxy_pool


def get_pool_list():
    prox, ip_list, length = proxy_pool.ip_pool()
    return [prox, ip_list, length]