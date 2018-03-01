#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int k=0;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i]){
                if (k!=i)
                    swap(nums[k],nums[i]);
                k++;
            }
        }
    }
};

int main()
{
    int n[] = {0, 0, 0, 3, 12};
    int size = sizeof(n)/sizeof(int);
    vector<int> v;
    for (int i = 0; i < size; ++i)
    {
        v.push_back(n[i]);
    }
    Solution s = Solution();
    s.moveZeroes(v);
    for (int i = 0; i < size; ++i)
    {
       cout<<v[i]<<" ";
    }
    return 0;
}