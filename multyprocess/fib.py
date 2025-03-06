from functools import reduce


def fibonacci(count):
    sequence = (0, 1)
    for _ in range(2, count):
        print(f"current index {_}")
        res = (reduce(lambda a, b: a + b, sequence[-2:]), )
        print(f"curret fib {res}")
        sequence += res
    return sequence[:count]

print(fibonacci(12))