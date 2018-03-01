
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

namespace p1 {
    class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int,int> m;
            vector<int> res;
            for (int i = 0; i < nums.size(); ++i) {
                if (m.find(nums[i])!=m.end()){
                    res.push_back(m[nums[i]]);
                    res.push_back(i);
                    return res;
                }
                m[target-nums[i]]=i;
            }
        }
    };
}