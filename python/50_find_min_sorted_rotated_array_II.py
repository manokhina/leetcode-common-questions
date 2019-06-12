"""
Question:
If the rotated sorted array could contain duplicates?
Is your algorithm still O(log n) in runtime complexity?
"""


class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        L = 0
        R = len(nums) - 1
        while L < R and nums[L] >= nums[R]:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[L]:
                R = M
            else:
                L += 1
        return nums[L]
