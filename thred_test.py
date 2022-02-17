import time
import threading
from python_test import blog_spider


def single_thread():
    for each in blog_spider.urls:
        blog_spider.spider(each)


def multi_thread():
    threads = []
    for each in blog_spider.urls:
        threads.append(threading.Thread(target=blog_spider.spider, args=(each,)))
    for each in threads:
        each.start()
    for each in threads:
        each.join()


if __name__ == '__main__':
    print("single_thread start")
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread end")
    print(end - start)

    print("multi_thread start")
    start2 = time.time()
    multi_thread()
    end2 = time.time()
    print("multi_thread end")
    print(end2 - start2)
