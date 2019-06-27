//Question:
//Given an array of integers, find two numbers such that they add up to
//a specific target number.
//The function twoSum should return indices of the two numbers such that
//they add up to the target, where index1 must be less than index2.
//Please note that your returned answers (both index1 and index2) are not zero-based.
//You may assume that each input would have exactly one solution.
//
//O(n) runtime, O(n) space – Hash table:
//We could reduce the runtime complexity of looking up a value to O(1) using a hash map
//that maps a value to its index.
#include <iostream>
#include <vector>
using namespace std;


vector<int> twoSum(vector<int> &numbers, int target)
{
    //Key is the number and value is its index in the vector.
    unordered_map<int, int> hash;
    vector<int> result;
    for (int i = 0; i < numbers.size(); i++) {
        int numberToFind = target - numbers[i];
        //if numberToFind is found in map, return them
        if (hash.find(numberToFind) != hash.end()) {
            //+1 because indices are NOT zero based
            result.push_back(hash[numberToFind] + 1);
            result.push_back(i + 1);
            return result;
        }
        //number was not found. Put it in the map.
        hash[numbers[i]] = i;
    }
    return result;
}
