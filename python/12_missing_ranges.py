"""
https://leetcode.com/problems/missing-ranges
Question:
Given a sorted integer array nums, where the range of elements are in the
inclusive range [lower, upper], return its missing ranges. For example,
given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]
Example Questions Candidate Might Ask:
Q: What if the given array is empty?
A: Then you should return [“0->99”] as those ranges are missing.
Q: What if the given array contains all elements from the ranges? A: Return an
empty list, which means no range is missing.
"""


class Solution:
    def missingRanges(self, nums: list, lower: int, upper: int) -> list:
        ranges = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 2:
                start = nums[i - 1] + 1
                end = nums[i] - 1
                ranges.append(f"{start}->{end}")
            elif nums[i] - nums[i - 1] == 2:
                single = nums[i - 1] + 1
                ranges.append(f"{single}")
        return ranges


if __name__ == "__main__":
    sol = Solution()
    print(sol.missingRanges([0, 2, 99], 0, 99))
    print(sol.missingRanges([], 1, 1))
    print(sol.missingRanges([8, 50, 67], 0, 99))
