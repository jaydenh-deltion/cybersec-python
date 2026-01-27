import concurrent.futures 
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp 
import itertools
import time

def attempt_match(length, target):
    for attempt in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=length):
        attempt = "".join(attempt)
        if attempt == target:
            print(f"[+] Password found: {attempt}")
            return attempt
        
if __name__ == "__main__":
    target = input("Enter password to crack:")
    Numb_of_cores = input("Enter number of CPU cores to use:")
    start_time = time.perf_counter()

    with ProcessPoolExecutor(max_workers=int(Numb_of_cores)) as executor:
        results = [executor.submit(attempt_match, length, target) for length in range(1, len(target) + 1)]

        for future in concurrent.futures.as_completed(results):
            match = future.result()
            if match:
                break 
            
    end_time = time.perf_counter()
    print(f"Password cracked in {end_time - start_time} seconds")


