#include <iostream>
#include <sstream>
#include <string>

class Solution {
public:
    std::string reverseWords(std::string s) {
        std::stringstream ss(s);
        std::string buf;        
        std::string result;
        while (ss >> buf) {
            result.insert(0, " ");
            result.insert(0, buf);
        }
        result.pop_back();
        return result;
    }
};
