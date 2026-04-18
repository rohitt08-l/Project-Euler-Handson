#Problem 31
def coin_sums(target):
    coins = [1,2,5,10,20,50,100,200]
    
    ways = [0] * (target + 1)
    
    ways[0] = 1   # base case

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[target]

print(coin_sums(200))