"""
Question:
Given a sorted array and a target value, return the index if the target
is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2 [1,3,5,6], 2 → 1 [1,3,5,6], 7 → 4 [1,3,5,6], 0 → 0
"""


class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        L = 0
        R = len(nums) - 1
        while L < R:
            M = (L + R) // 2
            if nums[M] < target:
                L = M + 1
            else:
                R = M
        return L + 1 if nums[L] < target else L
