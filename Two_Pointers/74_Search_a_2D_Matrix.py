"""74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start=0
        end=len(matrix)-1
        while start<=end:
            mid=(start+end)//2
            f=matrix[mid]
            l=0
            r=len(f)-1
            while l<=r:
                m=(l+r)//2
                if f[m]==target:
                    return True
                elif f[m]<target:
                    l=m+1
                else:
                    r=m-1
            if f[-1]<target:
                start=mid+1
            elif f[-1]>target:
                end=mid-1
        return False

