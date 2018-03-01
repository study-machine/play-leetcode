
#include <iostream>
#include <string>
#include <vector>

using namespace std;
namespace p76 {
    class Solution {
    public:
        string minWindow(string S, string T) {
            string res;
            int hash[256] = {0};
            for (int i = 0; i < T.size(); ++i)
                hash[T[i]]++;

            // like p438 hashCount to indicate if cover T's character
            int l = 0, r = 0, minCount = S.size() + 1, hashCount = T.size();
            while (r <= S.size()) {
                // if
                if (hashCount == 0) {
                    if (r - l < minCount) {
                        minCount = r - l;
                        res = S.substr(l, r - l);
                    }
                    if (hash[S[l]] >= 0)
                        hashCount++;
                    hash[S[l]]++;
                    l++;
                } else {
                    if (hash[S[r]] >= 1)
                        hashCount--;
                    hash[S[r]]--;
                    r++;
                }
            }

            return res;
        }
    };

}
