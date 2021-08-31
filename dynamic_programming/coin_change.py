"""

LC 322
"""
import math

def coinChange(coins,amount):
    """
    f(n) = min no. of coins needed to make up amount n 
    coins = [------]
            c1....ck
            
    f(n-c1)
    f(n-c2)
    ..
    .
    .
    .
    f(n-ck)

    Recurrence relation:
    f(n) = min{f(n-c1),f(n-c2)...f(n-ck)}+ 1

    """
    table = [math.inf]*(amount+1) # by defualt min no. of coins required is infinite
    table[0] = 0
    
    for i in range(1,amount+1):
        for c in coins:
            if i-c>=0:
                table[i] = min(table[i],table[i-c]+1)
                
    if(table[amount]==math.inf):
        return -1
    else:
        return table[amount]


print(coinChange([1,2,5],11))

