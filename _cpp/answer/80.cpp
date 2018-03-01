#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()==0)
            return 0;
        int k=0;
        int a=0;
        for (int i = 1; i < nums.size(); ++i)
        {
            if (nums[i]==nums[k] && a==0)
            {
                k++;
                nums[k]=nums[i];
                a=1;
            }
            if (nums[i]!=nums[k])
            {
                k++;
                nums[k]=nums[i];
                a=0;
            }
            
        }

        return k+1;
    }
};

int main()
{
    int arr[13]={1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5};
    vector<int> v(arr,arr+13);
    int res = Solution().removeDuplicates(v);
    cout<<"res:"<<res<<endl;

    for (int i = 0; i < v.size(); ++i)
    {
        cout<<v[i]<<" ";
    }
    return 0;
}