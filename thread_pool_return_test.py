from concurrent.futures import ThreadPoolExecutor


def dd(num):
    return num * 2


l1 = [1, 2, 3, 4, 5]


def hh(l1):
    with ThreadPoolExecutor() as t:
        for i in range(1, 5):
            results = t.map(dd, l1)
    return results


results = hh(l1)
for result in results:
    print(result)
