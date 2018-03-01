//
// Created by wxy on 2018/2/24.
//


#include <unordered_map>
#include <vector>

using namespace std;

namespace p447 {
    class Solution {
    public:
        int numberOfBoomerangs(vector<pair<int, int>> &points) {
            int res = 0;
            for (int i = 0; i < points.size(); ++i) {
                unordered_map<int, int> record;
                for (int j = 0; j < points.size(); ++j) {
                    if (i != j)
                        record[disPower(points[i], points[j])] += 1;
                }
                for (unordered_map<int, int>::iterator iter = record.begin(); iter != record.end(); iter++) {
                    res += iter->second * (iter->second - 1);
                }
            }
            return res;
        }

        int disPower(pair<int, int> &p1, pair<int, int> &p2) {
            return (p1.first - p2.first) * (p1.first - p2.first) +
                   (p1.second - p2.second) * (p1.second - p2.second);

        }
    };

}