#include <iostream>
#include <map>
#include <vector>

using namespace std;

namespace p350 {
    class Solution {
    public:
        vector<int> intersect(vector<int> &nums1, vector<int> &nums2) {
            map<int, int> record;
            for (int i:nums1)
                record[i]++;
            vector<int> res;
            for (int j:nums2)
                if (record[j] > 0) {
                    res.push_back(j);
                    record[j]--;
                }

            return res;
        }
    };

}