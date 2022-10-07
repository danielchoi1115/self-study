import time
def solution1(coins, quantity):
    hashtable = {}
    for coin, q in zip(coins, quantity):
        keys = list(hashtable)
        for i in range(1, q+1):
            price = coin*i
            for k in keys:
                hashtable.setdefault(k + price, None)
            hashtable.setdefault(price, None)
    return len(hashtable)


# Faster solution by benfei
def solution2(coins, quantity):
    possible_sums = {0}
    for c, q in zip(coins, quantity):
        possible_sums = {
            x + c * i for x in possible_sums 
            for i in range(q + 1)
        }
    
    return len(possible_sums) - 1

coins= [10, 50, 100]
quantity= [50000, 20, 10]

t1 = time.time()
print(solution1(coins, quantity))
print(time.time() - t1)

t1 = time.time()
print(solution2(coins, quantity))
print(time.time() - t1)