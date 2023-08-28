'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


'''

# 法ㄧ
def maxSubArray(nums):
    cursum = nums[0]
    value = [cursum]  # 初始化 value 列表
    for i in range(1, len(nums)):
        if nums[i] > cursum + nums[i]:
            cursum = nums[i]
        else:
            cursum += nums[i]
        value.append(cursum)
    return max(value)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) 



# 法二
def maxSubArray(nums):
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) 





