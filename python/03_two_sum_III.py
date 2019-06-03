"""
Question:
Design and implement a TwoSum class. It should support the following
operations: add and find.
add(input) – Add the number input to an internal data structure.
find(value) – Find if there exists any pair of numbers which sum is
equal to the value.

For example,
add(1); add(3); add(5); find(4) - true; find(7) - false
"""


class TwoSum:
    def __init__(self):
        self.structure = []

    def add(self, input):
        self.structure.append(input)

    def find(self, value):
        return self.twoSum(self.structure, value)

    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return True  # [hash_map[complement], i]
            else:
                hash_map[nums[i]] = i
        return False
