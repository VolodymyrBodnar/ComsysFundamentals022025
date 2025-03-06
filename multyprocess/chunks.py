from multiprocessing import Pool
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def chunk_sum(sublist):
    return sum(sublist)

def parallel_reduce(func, data, chunks=4):
    chunk_size = len(data) // chunks
    chunks_list = [data[i * chunk_size : (i + 1) * chunk_size] for i in range(chunks)]
    print(chunks_list)
    with Pool() as pool:
        partial_sums = pool.map(func, chunks_list)
    print(partial_sums)
    return reduce(lambda x,y: x + y, partial_sums)

total_sum = parallel_reduce(sum, numbers, chunks=4)
print(total_sum)  # Виведе: 36