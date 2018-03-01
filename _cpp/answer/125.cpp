#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int p1 = 0;
        int p2 = s.size() - 1;

        while (p1 < p2) {
            if (isNumAlpha(s[p1]) && isNumAlpha(s[p2])) {
                if (s[p1] == s[p2]) {
                    p1++;
                    p2--;
                } else if (s[p1] >= 65 && s[p2] >= 65 && s[p1] - s[p2] == 32 | s[p1] - s[p2] == -32) {
                    p1++;
                    p2--;
                } else
                    return false;
            }
            if (isNumAlpha(s[p1]) == false)
                p1++;
            if (isNumAlpha(s[p2]) == false)
                p2--;

        }
        return true;
    }

    bool isNumAlpha(char c) {
        if (c >= 48 & c <= 57 | c >= 65 & c <= 90 | c >= 97 & c <= 122)
            return true;
        else
            return false;
    }
};