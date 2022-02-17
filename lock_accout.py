import threading
import time


class Account:
    def __init__(self, balance):
        self.balance = balance


lock = threading.Lock()


def draw(account, amount):
    time.sleep(0.1)
    with lock:
        if account.balance >= amount:
            account.balance -= amount
            print(threading.current_thread().name, '取钱成功', f'余额:{account.balance}')
        else:
            print(threading.current_thread().name, '取钱失败', f'余额:{account.balance}')


acc = Account(1000)
t1 = threading.Thread(target=draw, args=(acc, 800), name='t1')
t2 = threading.Thread(target=draw, args=(acc, 800), name='t2')
t1.start()
t2.start()
