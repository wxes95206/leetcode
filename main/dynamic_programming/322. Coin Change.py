'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0






def coin_change(coins, amount):
    sorted_coins = sorted(coins, reverse=True)  # 將排序和賦值分開
    count = []
    for i in sorted_coins:
        count.append(amount // i )
        remainder = amount % i

        if remainder == 0:
            break
        else:
            amount = remainder
    

    return sum(count)
print(coin_change([2], 3))
'''

def coin_change(coins, amount):
    sorted_coins = sorted(coins, reverse=True)
    count = []
    for i in sorted_coins:
        count.append(amount // i)
        remainder = amount % i

        if remainder == 0:
            break
        else:
            amount = remainder
    else:
        if amount > 0:
            return -1
    
    return sum(count)

print(coin_change([2], 3))
