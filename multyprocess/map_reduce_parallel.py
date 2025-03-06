from multiprocessing import Pool
from functools import reduce
from collections import defaultdict


text_data = [
    "hello world hello",
    "map reduce example",
    "reduce map example example"
]

def map_function(text):
    words = text.split()
    return [(word, 1) for word in words]

with Pool() as pool:
    mapped_results = pool.map(map_function, text_data)

# Об’єднуємо всі результати з різних частин тексту
flat_mapped = [pair for sublist in mapped_results for pair in sublist]

def shuffle(mapped_data):
    grouped_data = defaultdict(list)
    print(grouped_data)
    for key, value in mapped_data:
        grouped_data[key].append(value)
        print(grouped_data)
    return grouped_data

def reduce_function(shuffled_data):
    return {key: reduce(lambda x,y: x+y ,values) for key, values in shuffled_data.items()}


shuffled = shuffle(flat_mapped)
reduced = reduce_function(shuffled)

print(reduced)
# Виведе: {'hello': 2, 'world': 1, 'map': 2, 'reduce': 2, 'example': 3}