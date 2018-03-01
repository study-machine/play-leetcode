//
// Created by wxy on 2018/2/16.
//

#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;
namespace p205 {
    class Solution {
    public:
        bool isIsomorphic(string s, string t) {
            map<char, char> m;
            set<char> u;

            if (s.size() != t.size())
                return false;
            for (int i = 0; i < s.size(); ++i) {
                if (m.find(s[i]) == m.end()) {
                    if (u.find(t[i]) != u.end())
                        return false;
                    m[s[i]] = t[i];
                    u.insert(t[i]);
                } else {
                    if (m[s[i]] != t[i])
                        return false;
                }
            }
            return true;
        }
    };
}