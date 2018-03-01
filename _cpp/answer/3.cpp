//
// Created by wxy on 2018/1/21.
//
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = -1, max_count = 0;
        int freq[256] = {0};

        while (l < s.size()) {
            if (r + 1 < s.size() && freq[s[r + 1]] == 0)
                freq[s[++r]]++;
            else
                freq[s[l++]]--;
            max_count = max(max_count, r - l + 1);
        }
        return max_count;
    }
};