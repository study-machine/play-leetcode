#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i]!=val)
                nums[k++]=nums[i];
        }
        return k;
    }
};


int main()
{
    int n[] = {3,2,2,3};
    int val = 3;
    vector<int> v;
    for (int i = 0; i < sizeof(n)/sizeof(int); ++i)
        v.push_back(n[i]);
    int r = Solution().removeElement(v,val);
    cout<<"res:"<<r<<endl;
    for (int i = 0; i < v.size(); ++i)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;
    return 0;
}