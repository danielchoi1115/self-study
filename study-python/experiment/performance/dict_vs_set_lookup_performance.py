import random
import time


def compare(size: int, iteration: int):
    """ Custom function which create dictionary and set of size `size` 
        and initializes with them with random integers

        It will perform element lookup `size` times and print time taken
    """

    # dict and set initialized with random integer
    d = {random.randint(0, 1000000000): None for _ in range(size)}
    s = set(d)
    print(f"iterate {iteration} times over dict and set of size {size}")
    
    t = time.time()
    for i in range(iteration): 
        check = i in d
    t2 = time.time()
    print("Dict lookup took", round(t2 - t, 4), "sec")


    t = time.time()
    for i in range(iteration): 
        check = i in s
    t2 = time.time()
    print("Set lookup took", round(t2 - t, 4), "sec taken")

if __name__ == "__main__":
    compare(100000, 1000000)
    
    compare(5000000, 50000000)
    
    compare(10000000, 100000000)
