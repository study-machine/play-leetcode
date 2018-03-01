//
// Created by wxy on 2018/2/25.
//

//
// Created by wxy on 2018/2/25.
//

//
// Created by wxy on 2018/2/24.
//


#include <unordered_set>
#include <unordered_map>
#include <vector>

using namespace std;

namespace p219 {
    class Solution {
    public:
        bool containsNearbyDuplicate(vector<int> &nums, int k) {
            unordered_set<int> record;
            for (int i = 0; i < nums.size(); ++i) {
                if (record.find(nums[i]) != record.end())
                    return true;
                record.insert(nums[i]);
                if (record.size() > k)
                    record.erase(nums[i - k]);
            }
            return false;
        }
    };

}