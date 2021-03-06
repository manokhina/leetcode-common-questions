"""
Question:
Given an array of integers, every element appears three times except for one.
Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?
"""


class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        a = b = 0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b
