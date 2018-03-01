#include <iostream>
#include <vector>
#include "../test_help.cpp"
using namespace std;
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int copy1[m];
        for (int i = 0; i < m; ++i)
            copy1[i]=nums1[i];
        int p1,p2 = 0;
        for (int i = 0; i < m+n; ++i){
            if (p1>=m){
                nums1[i]=nums2[p2];
                p2++;
            }else if(p2>=n){
                nums1[i]=copy1[p1];
                p1++;
            }else if(copy1[p1]<nums2[p2]){
                nums1[i]=copy1[p1];
                p1++;
            }else{
                nums1[i]=nums2[p2];
                p2++;
            }  
        }
    }
};


