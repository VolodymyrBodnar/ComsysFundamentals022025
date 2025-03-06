import multiprocessing
import time

COUNT = 50_000_000

def countdown(n):
    while n > 0:
        n -= 1

p1 = multiprocessing.Process(target=countdown, args=(COUNT//4,))
p2 = multiprocessing.Process(target=countdown, args=(COUNT//4,))

p3 = multiprocessing.Process(target=countdown, args=(COUNT//4,))
p4 = multiprocessing.Process(target=countdown, args=(COUNT//4,))



start = time.time()
p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

end = time.time()

print(f"Час виконання: {end - start:.2f} секунд")