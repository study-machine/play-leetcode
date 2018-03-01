#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int hash[256] = {0};
        for (int i = 0; i < p.size(); ++i)
            // ++ not =1,cuz character can be repeat
            hash[p[i]]++;
        vector<int> res;
        int l = 0, r = 0, count = p.size();
        while (r < s.size()) {
            if (hash[s[r]] >= 1)
                // find in hash first time
                count--;
            // decrease r's character in hash
            hash[s[r]]--;
            // increase r every time
            r++;
            if (count == 0)
                res.push_back(l);

            if (r - l == p.size()) {
                if (hash[s[l]] >= 0)
                    // add back count, cuz count has been decreased at r
                    count++;
                // reset hash
                hash[s[l]]++;
                // l has to move
                l++;
            }
        }
        return res;
    }
};