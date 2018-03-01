#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int sortColors(vector<int>& nums) {
        int a=-1;
        int c=nums.size();
        int i = 0;
        while (i<c){
            if (nums[i]<1 && i!=a)
            {
                swap(nums[i++],nums[++a]);

            }
            else if (nums[i]>1)
                swap(nums[i],nums[--c]);
            else
                i++;
        }
        return 0;
    }
};

int main(int argc, char const *argv[])
{
    int arr[6]={1,2,2,0,2,1};
    vector<int> v(arr,arr+6);
    int res = Solution().sortColors(v);

    for (int i = 0; i < v.size(); ++i)
    {
        cout<<v[i]<<" ";
    }
    return 0;
}