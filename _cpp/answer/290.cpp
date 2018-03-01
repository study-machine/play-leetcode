//
// Created by wxy on 2018/2/16.
//

#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;
namespace p290 {
    class Solution {
    public:
        bool wordPattern(string pattern, string str) {
            map<char, string> m;
            set<string> u;
            vector<string> str_vec = splitString(str);
            if (pattern.size() != str_vec.size())
                return false;
            for (int i = 0; i < pattern.size(); ++i) {
                if (m.find(pattern[i]) == m.end()) {
                    if (u.find(str_vec[i]) != u.end())
                        return false;
//                    m[pattern[i]] = str_vec[i];
                    m.insert(pair<char, string>(pattern[i], str_vec[i]));
                    u.insert(str_vec[i]);
                } else {
                    if (m[pattern[i]] != str_vec[i])
                        return false;
                }
            }
            return true;
        }

        vector<string> splitString(string str) {
            vector<string> res;
            int begin = 0, i = 0;
            while (i <= str.size()) {
                if (str[i] == ' ' || i == str.size()) {
                    res.push_back(str.substr(begin, i - begin));
                    begin = i + 1;
                }
                i++;
            }
            return res;
        }
    };
}