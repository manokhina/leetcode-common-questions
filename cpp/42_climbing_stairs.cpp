// // https://leetcode.com/problems/climbing-stairs/
// You are climbing a staircase.It takes n steps to reach the top.

//     Each time you can either climb 1 or
//     2 steps.In how many distinct ways can you climb to the top
//     ?

class Solution {
   public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 2, b = 1, res;
        for (int i = 3; i <= n; i++) {
            res = a + b;
            b = a;
            a = res;
        }
        return res;
    }
};