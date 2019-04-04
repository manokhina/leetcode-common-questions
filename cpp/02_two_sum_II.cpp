//Similar to Question [1. Two Sum], except that the input array is already
//sorted in ascending order.
//
//Solution:
//Of course we could still apply the [Hash table] approach, but it costs us
//O(n) extra space, plus it does not make use of the fact that the input is already sorted.
//
//O(n log n) runtime, O(1) space – Binary search:
//For each element x, we could look up if target – x exists in O(log n) time by applying
//binary search over the sorted array. Total runtime complexity is O(n log n).
//
//
//O(n) runtime, O(1) space – Two pointers:
//Let’s assume we have two indices pointing to the ith and jth elements, Ai and Aj
//respectively. The sum of Ai and Aj could only fall into one of these three possibilities:
//i. Ai + Aj > target. Increasing i isn’t going to help us, as it makes the sum even
//bigger. Therefore we should decrement j.
//ii. Ai + Aj < target. Decreasing j isn’t going to help us, as it makes the sum even
//smaller. Therefore we should increment i.
//iii. Ai + Aj == target. We have found the answer.

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        int i = 0;
        int j = nums.size() - 1;
        while (i < j) {
            if (nums[i] + nums[j] > target) {
                j -= 1;
            } else if (nums[i] + nums[j] < target) {
                i += 1;
            } else if (nums[i] + nums[j] == target) {
                result.push_back(i + 1);
                result.push_back(j + 1);
                return result;
            }
        }
    }
};
