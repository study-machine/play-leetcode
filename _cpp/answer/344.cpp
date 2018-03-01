//
// Created by wxy on 2018/1/21.
//

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string reverseString(string s) {
        int p1 = 0;
        int p2 = s.size() - 1;

        while (p1 < p2) {
            swap(s[p1], s[p2]);
            p1++;
            p2--;
        }
        return s;
    }
};