//
// Created by wxy on 2018/1/21.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int l = 0;
        int r = height.size()-1;

        int maxArea = 0;
        while (l < r) {
            int lh = height[l];
            int rh = height[r];
            int area = min(lh, rh) * (r - l);
            if (area > maxArea)
                maxArea = area;
            if (lh < rh)
                l++;
            else
                r--;
        }
        return maxArea;
    }
};
