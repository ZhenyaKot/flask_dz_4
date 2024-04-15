# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
#  Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
#  Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
#  При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
#  В каждом решении нужно вывести время выполнения
# вычислений.

# НА СЕМЕНАРЕ ВЫ СКАЗАЛИ СДАТЬ ЭТО ЗАДАНИЕ
import time
import threading
import random

start_time = time.time()
array = [random.randint(1, 100) for _ in range(1_000_000)]


def colculate_sum(lst, result_list):
    total_sum = sum(lst)
    result_list.append(total_sum)


threads = []

chunk_size = 1000

results = []

for i in range(0, len(array), chunk_size):
    chunk = array[i: i + chunk_size]
    result_list = []
    t = threading.Thread(target=colculate_sum, args=(chunk, result_list))
    threads.append(t)
    t.start()
    results.append(result_list)

for t in threads:
    t.join()
total_sum = sum(sum(result) for result in results)

print(f'время вычисления равно {time.time() - start_time}')
print(f'Итоговая сумма: {total_sum}')
