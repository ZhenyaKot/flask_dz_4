import asyncio
import time
import random

start_time = time.time()
array = [random.randint(1, 100) for _ in range(1_000_000)]


async def calculate_sum(lst, result_list):
    total_sum = sum(lst)
    result_list.append(total_sum)


async def main():
    tasks = []
    chunk_size = 1000
    results = []
    for i in range(0, len(array), chunk_size):
        chunk = array[i: i + chunk_size]
        result_list = []
        task = asyncio.create_task(calculate_sum(chunk, result_list))
        tasks.append(task)
        results.append(result_list)
    await asyncio.gather(*tasks)
    total_sum = sum(sum(result) for result in results)
    print(f'Итоговая сумма: {total_sum}')
if __name__ == '__main__':
    asyncio.run(main())
    print(f'время вычисления равно {time.time() - start_time}')

