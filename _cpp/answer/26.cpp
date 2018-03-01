#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()==0)
            return 0;
        int k=0;

        for (int i = 1; i < nums.size(); ++i)
        {
            if (nums[i]!=nums[k]){
                nums[++k]=nums[i];
            }
        }

        return k+1;
    }
};

int main(int argc, char const *argv[])
{
    int arr[10]={1,2,2,2,3,3,3,3,3,4};
    vector<int> v;
    int res = Solution().removeDuplicates(v);
    cout<<"res:"<<res<<endl;

    for (int i = 0; i < v.size(); ++i)
    {
        cout<<v[i]<<" ";
    }
    return 0;
}