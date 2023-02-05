#include <iostream>
#include <sstream>
#include <string>
#include <vector>

// Rotate a string to the right by k words in-place without allocating extra
// space. For instance, with k = 3, the string "the sky is blue" is rotated to
// "sky is blue the".
// For instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to
// [4, 5, 6, 0, 1, 2, 3].

class Solution {
   public:
    std::string reverseWords2(std::string s, int k) {
        std::stringstream ss(s);
        std::string buf;
        std::string result;
        while (ss >> buf) {
            if (k > 0) result.insert(0, " ");
            result.insert(0, buf);
            k--;
        }
        result.pop_back();
        return result;
    }
};

int main() {
    Solution solution;
    std::cout << solution.reverseWords2("the sky is blue", 3) << std::endl;
    return 0;
}