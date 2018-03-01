//
// Created by wxy on 2018/2/14.
//

#include <iostream>
#include <map>
#include <vector>

using namespace std;

namespace p242 {
    class Solution {
    public:
        bool isAnagram(string s, string t) {
            int hash[256] = {0};
            for (int i = 0; i < t.size(); ++i)
                hash[t[i]]++;
            int hashCount = static_cast<int>(t.size());
            for (int j = 0; j < s.size(); ++j) {
                if (hash[s[j]] <= 0) {
                    return false;
                } else {
                    hash[s[j]]--;
                    hashCount--;
                }

            }
            return hashCount == 0;

        }
    };

    class Solution2 {
    public:
        bool isAnagram(string s, string t) {
            int hash[26] = {0};
            for (int i = 0; i < s.size(); ++i)hash[s[i] - 'a']++;
            for (int j = 0; j < t.size(); ++j)hash[t[j] - 'a']--;
            for (int i = 0; i < 26; ++i)if (hash[i] != 0)return false;
            return true;
        }
    };
}