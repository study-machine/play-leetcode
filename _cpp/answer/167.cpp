#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        vector<int> v(2);
        if (numbers.size() == 0)
            return v;
        while (true) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) {
                v[0] = l + 1;
                v[1] = r + 1;
                return v;
            }
            if (sum>target)
                r--;
            else
                l++;
        }

    }
};

