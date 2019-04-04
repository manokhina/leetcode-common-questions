//Question:
//Design and implement a TwoSum class. It should support the following
//operations: add and find.
//add(input) – Add the number input to an internal data structure.
//find(value) – Find if there exists any pair of numbers which sum is
//equal to the value.
//
//For example,
//add(1); add(3); add(5); find(4) - true; find(7) - false
#include <iostream>
#include <vector>
using namespace std;

class TwoSum {
private:
    vector<int> data;
public:
    void add(int number) {
        data.insert(number);
    }
    bool find(int value) {
        unordered_map<int, int> hash;
        for (int i = 0; i < data.size(); i++) {
            int numberToFind = target - data[i];
            //if numberToFind is found in map, return them
            if (hash.find(numberToFind) != hash.end()) {
                return true;
            }
            //number was not found. Put it in the map.
            hash[data[i]] = i;
        }
        return false;
    }
};