# Definition for singly-linked list.
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None


from singlelink import SinCycLinkedlist

class Solution(object):
    def __init__(self):
        self._head = None
        # self.l1 = l1
        # self.l2 = l2

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def append(self, item):
        """尾部添加节点"""
        node = ListNode()
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 移到链表尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self._head

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print(cur.val)
        while cur.next != self._head:
            cur = cur.next
            print(cur.val)
        print("")

    def print_ListNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next

class test:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head1 = l1
        head2 = l2
        flag = 0
        print(head1.next)
        print(head2.next)

        while head1.next is not None or head2.next is not None:
            # 存在某一链表next为空时，构造next.val = 0，不影响加法结果
            if head1.next is None:
                head1.next = ListNode()
            if head2.next is None:
                head2.next = ListNode()

            sumNum = head1.val + head2.val
            if sumNum >= 10:
                head1.val = sumNum % 10
                flag = 1
                head1.next.val += 1
            else:
                head1.val = sumNum
                flag = 0
            head1 = head1.next
            head2 = head2.next
        else:
            # 链表末尾时，单独处理，其和大于10时，追加节点
            head1.val = head1.val + head2.val
            print('1', type(head1.val))
            print('2', head1.val)
            if head1.val >= 10:
                head1.val = head1.val % 10
                head1.next = ListNode()
        return l1



        # -------------------------------
        # self.d = 0
        # def sums(a, b):
        #     c = a + b
        #     if self.d == 1:
        #         c += 1
        #         self.d = 0
        #     if c >= 10:
        #         c = c-10
        #         self.d = 1
        #
        #     return c
        #
        # # l1.reverse()
        # # l2.reverse()
        #
        # res = list(map(sums, l1, l2))
        # # res.reverse()
        # return res


if __name__ == "__main__":
    ls = ListNode()
    l1 = Solution()
    l2 = Solution()
    lens = l1.length()
    lens2 = l2.length()
    print(lens)
    print(lens2)
    list1 = [2,3,7,5]
    list2 = [4,6,2]
    for i in list1:
        l1.append(i)
    for i in list2:
        l2.append(i)

    print(l1.length())
    print(l2.length())
    print(l1, type(l1), l2)
    print(l1.print_ListNode(ls))
    l3 = test()
    # l3.addTwoNumbers(l1, l2)






