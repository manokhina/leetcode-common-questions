//Question:
//Given a string, determine if it is a palindrome, considering only
//alphanumeric characters and ignoring cases.
//For example,
//"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.
//Example Questions Candidate Might Ask:
//Q: What about an empty string? Is it a valid palindrome?
//A: For the purpose of this problem, we define empty string as valid palindrome.
#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string s) {
    for (int i = 0, j = s.size() - 1; i < j; i++, j--) { // Move 2 pointers from each end until they collide
        while (isalnum(s[i]) == 0 && i < j) i++; // Increment left pointer if not alphanumeric
        while (isalnum(s[j]) == 0 && i < j) j--; // Decrement right pointer if no alphanumeric
        if (toupper(s[i]) != toupper(s[j])) return false; // Exit and return error if not match
    }
    return true;
}