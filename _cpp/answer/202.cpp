//
// Created by wxy on 2018/2/15.
//
#include <set>

using namespace std;
namespace p202 {
    class Solution {
    public:
        bool isHappy(int n) {
            set<int> s;
            while (n != 1) {
                n = countN(n);
                if (s.find(n) == s.end())
                    s.insert(n);
                else
                    return false;
            }
            return true;
        }

        int countN(int n) {
            int res = 0, tmp;
            while (n != 0) {
                tmp = (n % 10);
                res += tmp * tmp;
                n = n / 10;
            }
            return res;
        }
    };
}