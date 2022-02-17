import threading
import time

import blog_spider
import queue
import random


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.spider(url)
        html_queue.put(html)
        print(threading.current_thread().name, f'craw {url}', f'url_queue_size {url_queue.qsize()}')
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + '\n')
        print(threading.current_thread().name, f'html_queue_size {html_queue.qsize()}', 'results_size:', len(results))
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)
    for idx in range(40):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f'craw{idx}')
        t.start()
    fout = open('./data.txt', 'w')

    for idx in range(20):
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f'parse{idx}')
        t.start()
