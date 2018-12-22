"""
Similar to Question [1. Two Sum], except that the input array is already
sorted in ascending order.

Solution:
Of course we could still apply the [Hash table] approach, but it costs us
O(n) extra space, plus it does not make use of the fact that the input is already sorted.

O(n log n) runtime, O(1) space – Binary search:
For each element x, we could look up if target – x exists in O(log n) time by applying
binary search over the sorted array. Total runtime complexity is O(n log n).


O(n) runtime, O(1) space – Two pointers:
Let’s assume we have two indices pointing to the ith and jth elements, Ai and Aj
respectively. The sum of Ai and Aj could only fall into one of these three possibilities:
i. Ai + Aj > target. Increasing i isn’t going to help us, as it makes the sum even
bigger. Therefore we should decrement j.
ii. Ai + Aj < target. Decreasing j isn’t going to help us, as it makes the sum even
smaller. Therefore we should increment i.
iii. Ai + Aj == target. We have found the answer.
"""


class SolutionI:
    def two_sum_sorted(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            j = self.binary_search(nums, target - nums[i],  i + 1)
            if j != -1:
                return [i + 1, j + 1]

    @staticmethod
    def binary_search(nums, key, start):
        left = start
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < key:
                left = mid + 1
            else:
                right = mid
        if left == right and nums[left] == key:
            return left
        else:
            return -1


class SolutionII:
    def two_sum_sorted(self, nums, target):
        """
        Two pointers solution
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] == target:
                return [i + 1, j + 1]
