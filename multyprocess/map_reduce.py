from collections import defaultdict
from functools import reduce

def map_function(text):
    words = text.split()
    return list(map(lambda word: (word, 1), words))


def shuffle(mapped_data):
    grouped_data = defaultdict(list)
    print(grouped_data)
    for key, value in mapped_data:
        grouped_data[key].append(value)
        print(grouped_data)
    return grouped_data

def reduce_function(shuffled_data):
    return {key: reduce(lambda x,y: x+y ,values) for key, values in shuffled_data.items()}


text = "hello world hello"
mapped = map_function(text)
shuffled = shuffle(mapped)
print(shuffled)
reduced = reduce_function(shuffled)
print(reduced)
# Виведе: {'hello': 2, 'world': 1}
# Виведе: {'hello': [1, 1], 'world': [1]}