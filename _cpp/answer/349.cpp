#include <iostream>
#include <set>
#include <vector>

using namespace std;

namespace p349 {
    class Solution {
    public:
        vector<int> intersection(vector<int> &nums1, vector<int> &nums2) {
            set<int> s1(nums1.begin(), nums1.end());
            set<int> res;
            for (int i : nums2)
                if (s1.find(i) != s1.end())
                    res.insert(i);

            return vector<int>(res.begin(), res.end());
        }
    };
}