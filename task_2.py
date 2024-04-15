import time
import multiprocessing
import random

start_time = time.time()
array = [random.randint(1, 100) for _ in range(1_000_000)]


def calculate_sum(lst, result_list):
    total_sum = sum(lst)
    result_list.append(total_sum)


if __name__ == '__main__':
    processes = []
    chunk_size = 1000
    results = []

    for i in range(0, len(array), chunk_size):
        chunk = array[i: i + chunk_size]
        result_list = []
        p = multiprocessing.Process(target=calculate_sum, args=(chunk, result_list))
        processes.append(p)
        p.start()
        results.append(result_list)

    for p in processes:
        p.join()

    total_sum = sum(sum(result) for result in results)

    print(f'время вычисления равно {time.time() - start_time}')
    print(f'Итоговая сумма: {total_sum}')