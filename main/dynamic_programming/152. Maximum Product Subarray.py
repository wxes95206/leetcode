'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

'''
(negative)*(negative) = positive
'''




def maxProduct(n):
    if len(n) == 0:
        return 0

    pos_max = n[0]
    neg_min = n[0]
    max_product_result = n[0]

    for i in range(1, len(n)):
        if n[i] < 0:
            pos_max, neg_min = neg_min, pos_max  # 交換最大正乘積和最小負乘積
        pos_max = max(n[i], pos_max * n[i])
        neg_min = min(n[i], neg_min * n[i])
        max_product_result = max(max_product_result, pos_max)

    return max_product_result

print(maxProduct([-2,0,-1]))
