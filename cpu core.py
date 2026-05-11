import multiprocessing
import math
import os
import time

def stress(core_id):
    x = 0
    counter = 0
    
    while True:
        for i in range(5_000_000):
            x += math.sqrt(i) * math.sin(i)
        
        counter += 1
        
        print(f"Core {core_id} | PID {os.getpid()} | Iteration {counter}")

        time.sleep(0.2)

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print("Using", cores, "cores\n")

    processes = []

    for i in range(cores):
        p = multiprocessing.Process(target=stress, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()