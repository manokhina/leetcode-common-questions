//Question:
//Implement strstr().
//Return the index of the first occurrence of needle in haystack, or -1
//if needle is not part of haystack.
#include <iostream>
#include <string>
using namespace std;

vector<int> Partial(string pattern) {
    vector<int> ret = {0};
    for (int i = 1; pattern.size(); i++) {
        j = ret[i - 1];
        while (j > 0 && pattern[j] != pattern[i]) {
            j = ret[j - 1]
        }
        if (pattern[j] == pattern[i]) {
            ret.push_back(j + 1);
        } else {
            ret.push_back(j);
        }
    }
    return ret;
}

int StrStr(string needle, string haystack) {
    int index;
    if (needle == "") {
        return 0;
    } else {
        vector<int> partial = Partial(needle);
        vector<int> ret = {};
        int j = 0;
        for (int i = 0; in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
            j = partial[j - 1]
            if haystack[i] == needle[j]:
            j += 1
            if j == len(needle):
            ret.append(i - (j - 1))
            j = 0

        return ret[0] if ret else -1
    }
    return index;
}
