//
// Created by wxy on 2018/2/13.
//

#ifndef UNTITLED_RUN_H
#define UNTITLED_RUN_H

#include "answer/76.cpp"
#include "answer/242.cpp"
#include "answer/349.cpp"
#include "answer/350.cpp"
#include "answer/202.cpp"
#include "answer/290.cpp"
#include "answer/205.cpp"
#include "answer/451.cpp"
#include "answer/1.cpp"
#include "answer/447.cpp"
#include "answer/217.cpp"
#include "answer/219.cpp"
#include "answer/220.cpp"

using namespace std;

void run_1() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> res = p1::Solution().twoSum(nums, target);
    for (int i :res) {
        cout << i << ",";
    }
}

void run_217() {
    vector<int> nums = {2, 7, 11, 15, 2};
    bool res = p217::Solution().containsDuplicate(nums);
    cout << res << ",";
}

void run_219() {
    vector<int> nums = {2, 7, 11, 15, 2, 3};
    bool res = p219::Solution().containsNearbyDuplicate(nums,3);
    cout << res << ",";
}
void run_220() {
    vector<int> nums = {0,2147483647};
    bool res = p220::Solution().containsNearbyAlmostDuplicate(nums,1,2147483647);
    cout << res << ",";
}
void run_447() {
    // [[0,0],[1,0],[2,0]]
    pair<int, int> p1(0, 0);
    pair<int, int> p2(1, 0);
    pair<int, int> p3(2, 0);
    vector<pair<int, int>> points = {p1, p2, p3};
    int res = p447::Solution().numberOfBoomerangs(points);
    cout << res;
}

void run_76() {
//    string S = "ADOBECODEBANC";
//    string T = "ABC";
    string S = "a";
    string T = "a";
    string res = p76::Solution().minWindow(S, T);
    cout << res;

}

void run_451() {
    string s = "tree";
    string res = p451::Solution().frequencySort(s);
    cout << res;

}

void run_202() {
    int n = 19;
    cout << p202::Solution().isHappy(n);
}

void run_205() {
    string s = "ab";
    string t = "aa";
    cout << p205::Solution().isIsomorphic(s, t);

}

void run_290() {
    string pattern = "abba";
    string _str = "dog cat cat dog";
    cout << p290::Solution().wordPattern(pattern, _str);

}

void run_242() {
    //s = "anagram", t = "nagaram", return true.
    string S = "anagram";
    string T = "nagaram";
    bool res = p242::Solution2().isAnagram(S, T);
    cout << res;
}

void run_349() {
    vector<int> nums1 = {1, 2, 2, 1};
    vector<int> nums2 = {2, 2};
    vector<int> res = p349::Solution().intersection(nums1, nums2);
    for (int i :res) {
        cout << i << ",";
    }
}

void run_350() {
    vector<int> nums1 = {1, 2, 2, 1};
    vector<int> nums2 = {2, 2};
    vector<int> res = p350::Solution().intersect(nums1, nums2);
    for (int i :res) {
        cout << i << ",";
    }
}


#endif //UNTITLED_RUN_H
