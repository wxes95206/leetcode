"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""



"""
「爬第 n 階樓梯的方法數」等於「爬上 n−1 階樓梯的方法數量」 + 「爬上 n−2 階樓梯的方法數量」


迭代到 i = 3 時，我們計算 W[3] = W[1] + W[2] = 1 + 2 = 3，所以此時 W 變成 [0, 1, 2, 3]。

迭代到 i = 4 時，我們計算 W[4] = W[2] + W[3] = 2 + 3 = 5，所以此時 W 變成 [0, 1, 2, 3, 5]。

迭代到 i = 5 時，我們計算 W[5] = W[3] + W[4] = 3 + 5 = 8，所以最終 W 變成 [0, 1, 2, 3, 5, 8]。
"""


# 法一
def climbStairs(n):
        W = [0, 1, 2]
        for i in range(3, n+1):
            W.append( W[i - 2] + W[i - 1])
        return W[n]

print(climbStairs(5))



# 法二
(Fibonacci series)

'''
1 step --> ans: 1
2 steps--> ans: 2
  1+1
  2   
3 steps --> ans:3  
  1+1+1
  1+2
  2+1
4 steps --> ans:5
  1+1+1+1
  1+2+1
  1+1+2
  2+1+1
  2+2

Fn = Fn-1 + Fn-2
            

'''
def climbstarirs(n):
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[-1]

print(climbstarirs(5))
