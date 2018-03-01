//
// Created by wxy on 2018/2/16.
//

#include <set>
#include <map>
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;
namespace p451 {
    class Solution {
    public:
        string frequencySort(string s) {
            unordered_map<char,int> freq;
            vector<string> bucket(s.size()+1, "");
            string res;

            //count frequency of each character
            for(char c:s) freq[c]++;
            //put character into frequency bucket
            for(auto& it:freq) {
                int n = it.second;
                char c = it.first;
                bucket[n].append(n, c);
            }
            //form descending sorted string
            for(int i=s.size(); i>0; i--) {
                if(!bucket[i].empty())
                    res.append(bucket[i]);
            }
            return res;
        }
//        string frequencySort(string s) {
//            vector<string> tmp(5);
//            tmp[1].append("Aa",30);
//            cout<<tmp[1];
//        }
    };
}