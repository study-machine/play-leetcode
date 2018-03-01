//
// Created by wxy on 2018/2/25.
//

//
// Created by wxy on 2018/2/24.
//


#include <unordered_set>
#include <vector>

using namespace std;

namespace p217 {
    class Solution {
    public:
        bool containsDuplicate(vector<int> &nums) {
            unordered_set<int> record;
            for (int i = 0; i < nums.size(); ++i) {
                if (record.find(nums[i]) != record.end())
                    return true;
                record.insert(nums[i]);
            }
            return false;
        }
    };

}