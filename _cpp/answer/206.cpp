//
// Created by wxy on 2018/2/25.
//
#define NULL 0


struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};
namespace p226 {
    class Solution {
    public:
        ListNode *reverseList(ListNode *head) {
            ListNode *pre = NULL;
            ListNode *cur = head;
            while (cur != NULL) {
                ListNode *next = cur->next;
                cur->next = pre;
                pre = cur;
                cur = next;
            }
            return pre;
        }
    };
}