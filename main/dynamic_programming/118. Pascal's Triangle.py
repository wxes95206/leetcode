"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

https://leetcode.com/problems/pascals-triangle/
 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]



"""
'''
    1
   1,1
  1,2,1
 1,3,3,1
1,4,6,4,1


'''

def pascal_tri(n):
    triangle =[[1],[1,1]]
    for i in range(2,n):
        row = [1]
        for j in range(1,i):
            row.append(triangle[i-1][j-1]+triangle[i-1][j]) 
        row.append(1)
        triangle.append(row)
    return triangle

print(pascal_tri(5))
'''
1. 當 i 從 2 開始迭代時，我們已經有了前兩行（即索引 0 和 1 的行），所以我們只需要生成從索引 2 開始的行，一直到索引 n-1(總共 n-2 行）。
這就是為什麼迴圈的範圍是 (2, n)，而不是 (2, n+1)


2.在內部迴圈中，當從 triangle 清單中取得元素時，應該使用 triangle[i - 1]，而不是 triangle[i]，因為清單索引從 0 開始

'''
