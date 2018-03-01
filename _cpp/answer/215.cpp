#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
       int l = 0;
       int r = nums.size()-1;
       int p = 0;
       while(true){
            p = partition(nums,l,r);
            if (p==k-1)
                return nums[p];
            if(p<k-1)
                l=p+1;
            else
                r=p-1;
       }

    }

    int partition(vector<int>& arr,int l,int r){
        int e = arr[l];
        int lt = r;
        int gt = l+1;
        while (lt>=gt){
            if (arr[lt]>e && arr[gt]<e)
                swap(arr[lt],arr[gt]);
            if (arr[lt]<=e)
                lt--;
            if (arr[gt]>=e)
                gt++;
        }
        swap(arr[l],arr[lt]);
        return lt;
    }
};