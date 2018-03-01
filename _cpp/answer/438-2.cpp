//
// Created by wxy on 2018/2/13.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        int hash[256] = {0};
        for (int i = 0; i < p.size(); ++i)
            hash[p[i]]++;

        int l = 0, r = 0, count = p.size();

        while (r < s.size()) {
            if (hash[s[r]] >= 1)
                count--;
            hash[s[r]]--;
            r++;
            if (count == 0)
                res.push_back(l);
            if (r - l == p.size()) {
                if (hash[s[l]] >= 0)
                    count++;
                hash[s[l]]++;
                l++;
            }
        }

        return res;
    }

};