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


def max_product(n):
    pos_pro_list = []
    neg_pro_list = []
    zero_list = []

    for i in range(1, len(n)):
        if n[i - 1] * n[i] > 0:
            pos_pro_list.append(n[i - 1] * n[i])
        elif n[i - 1] * n[i] < 0:
            neg_pro_list.append(n[i - 1] * n[i])
        else:
            zero_list.append(n[i - 1] * n[i])
        
        output = max(pos_pro_list,zero_list)
        return max(output)

print(max_product([2,3,-2,4]))  
