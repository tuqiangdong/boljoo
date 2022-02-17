import request_reconn_binary


def thread_down_gif_fun(seq, name, fan_name, prox, ip_list,length, src, head, reconn_num, time_out):
    binary = request_reconn_binary.request_reconn_fun(prox, ip_list, length, src, head, 3, 30)
    with open(f'./test/{name}/{fan_name}/{seq}.gif', 'wb') as f:
        f.write(binary)

