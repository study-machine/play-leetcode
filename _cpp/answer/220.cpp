//
// Created by wxy on 2018/2/25.
//

//
// Created by wxy on 2018/2/25.
//

//
// Created by wxy on 2018/2/25.
//

//
// Created by wxy on 2018/2/24.
//


#include <set>
#include <vector>
#include <iostream>

using namespace std;

namespace p220 {
    class Solution {
    public:
        bool containsNearbyAlmostDuplicate(vector<int> &nums, int k, int t) {
            set<long long> record;

            for (int i = 0; i < nums.size(); ++i) {
                int v = nums[i];
                long long vl = (long long)v;
                long long tl = (long long)t;
                if (record.lower_bound(vl - tl) != record.end() &&
                    *record.lower_bound(vl - tl) <= vl + tl)
                    return true;
                record.insert(nums[i]);
                if (record.size() > k)
                    record.erase(nums[i - k]);
            }
            return false;
        }
    };

}