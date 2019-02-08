"""
Question:
Given an array of integers, every element appears twice except for one.
Find that single one.
Example Questions Candidate Might Ask:
Q: Does the array contain both positive and negative integers? A: Yes.
Q: Could any element appear more than twice? A: No.
"""


class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        map = dict()
        for x in nums:
            count = map[x] or 0
            map[x] = count + 1
        for x in nums:
            if map[x] == 1:
                return x
        return "No single element"
