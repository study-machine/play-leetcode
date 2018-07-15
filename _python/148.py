class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val) if self.val is not None else 'null'


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.quickSort(head, None)

    def quickSort(self, start, end):
        if start is end or start.next is end:
            return start

        cur = start
        left = start

        while cur and cur is not end:
            if cur.next and cur.next.val < start.val:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = left
                left = tmp
            else:
                cur = cur.next
        left = self.quickSort(left, start)
        start.next = self.quickSort(start.next, end)
        return left


def create_list(l):
    dummyHead = ListNode(0)
    curNode = dummyHead
    for x in l:
        curNode.next = ListNode(x)
        curNode = curNode.next
    return dummyHead.next


def print_list(head):
    curNode = head
    while curNode:
        print curNode.val,
        curNode = curNode.next
    print ''


from random import randint, shuffle

if __name__ == '__main__':
    l = list(range(1, 5))
    shuffle(l)
    # l = [4,5,3,2,1,2,3,4,5]
    l = [2, 3, 4, 1]
    head = create_list(l)
    print l
    # print_list(head)
    print
    new_head= Solution().sortList(head)

    print 'res'
    print_list(new_head)
