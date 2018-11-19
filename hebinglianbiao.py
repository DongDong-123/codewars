# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#     # def add(self, elem):
#     #     nodes = ListNode(elem)
#     #     nodes.next = self.val
#     #     self.val = nodes
#     #     # return nodes
#
#
# class Solution():
#     def __init__(self):
#         self._head = None
#
#     def add(self, item):
#         """尾部添加元素"""
#         node = ListNode(item)
#         # 先判断链表是否为空，若是空链表，则将_head指向新节点
#         if self.is_empty():
#             self._head = node
#             node.next = None
#         # 若不为空，则找到尾部，将尾节点的next指向新节点
#         else:
#             cur = self._head
#             print(cur.val)
#             while cur.next != None:
#                 cur = cur.next
#                 print('cur', cur.val)
#
#             cur.next = node
#
#     def is_empty(self):
#         """判断链表是否为空"""
#         return self._head == None
#
#     def travel(self):
#         """遍历链表"""
#         if self.is_empty():
#             return
#         cur = self._head
#         print('cur.val',cur.val)
#         while cur.next != None:
#             cur = cur.next
#             print('cur.val', cur.val)
#
#         print("")
#
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         newnode = Solution()
#         cur1 = l1._head
#         cur2 = l2._head
#         print(cur1.val, cur2.val)
#         while (cur1 != None) and (cur2 != None):
#             if cur1.val < cur2.val:
#                 newnode.add(cur1.val)
#                 cur1 = cur1.next
#             elif cur1.val > cur2.val:
#                 newnode.add(cur2.val)
#                 cur2 = cur2.next
#             else:
#                 newnode.add(cur1.val)
#                 newnode.add(cur2.val)
#                 cur1 = cur1.next
#                 cur2 = cur2.next
#         else:
#             if cur1 == None:
#                 while cur2 != None:
#                     newnode.add(cur2.val)
#                     cur2 = cur2.next
#
#             elif cur2 == None:
#                 while cur1 != None:
#                     newnode.add(cur1.val)
#                     cur1 = cur1.next
#
#         return newnode
#
#
#
#
#
#
# if __name__ == "__main__":
#     ll = Solution()
#     ll.add(2)
#     ll.add(6)
#     ll.add(9)
#     ll.add(14)
#     ll.add(36)
#     ll.travel()
#
#     node2 = Solution()
#     node2.add(3)
#     node2.add(8)
#     node2.add(9)
#     node2.add(12)
#     node2.add(22)
#     node2.add(35)
#     node2.travel()
#
#     res = Solution()
#     tt = res.mergeTwoLists(ll,node2)
#
#     print("-----------------------")
#     tt.travel()
# #     # node3 = ListNode(None)
# #     # print(node3)
# #     # node3.next = 3
# #     # node3.next = 5
# #     # print(node3.val)
#
# # class Node:
# #     """创建节点"""
# #     def __init__(self, item):
# #         self.item = item  # item存放数据元素
# #         self.next = None  # next 下一个节点的标识
# #
# #
# # class SingleLinkList:
# #     """单向循环链表"""
# #
# #     def __init__(self):
# #         self._head = None
# #
# #     def is_empty(self):
# #         """判断链表是否为空"""
# #         return self._head == None
# #
# #     def length(self):
# #         """返回链表的长度"""
# #         # 如果链表为空，返回长度0
# #         if self.is_empty():
# #             return 0
# #         count = 1
# #         # 创建一个游标，指向头节点，从头遍历到尾部
# #         cur = self._head
# #         while cur.next != None:
# #             count += 1
# #             cur = cur.next
# #         return count
# #
# #     def travel(self):
# #         """遍历链表"""
# #         if self.is_empty():
# #             return
# #         cur = self._head
# #         print(cur.item)
# #         while cur.next != None:
# #             cur = cur.next
# #             print(cur.item)
# #
# #     def add(self, item):
# #         """头部添加节点"""
# #         # 先创建一个节点，保存item值
# #         node = Node(item)
# #         # 将新节点的链接域next指向头节点，即_head指向的位置
# #         node.next = self._head
# #         # 将链表的头_head指向新节点
# #         self._head = node
# #
# #     def append(self, item):
# #         """尾部添加元素"""
# #
# #         node = Node(item)
# #         # 先判断链表是否为空，若是空链表，则将_head指向新节点
# #         if self.is_empty():
# #             self._head = node
# #         # 若不为空，则找到尾部，将尾节点的next指向新节点
# #         else:
# #             cur = self._head
# #             while cur.next != None:
# #                 cur = cur.next
# #             # 将尾节点的next指向新节点
# #             cur.next = node
# #
# #     def insert(self, pos, item):
# #         """
# #         在指定位置添加节点
# #         :type pos: int
# #         :type item: elememt
# #         """
# #         # 若指定位置pos为第一个元素之前，则执行头部插入
# #         if pos <= 0:
# #             self.add(item)
# #         # 若指定位置超过链表尾部，则执行尾部插入
# #         elif pos > (self.length() - 1):
# #             self.append(item)
# #         # 链表中的其他位置
# #         else:
# #             node = Node(item)
# #             cur = self._head
# #             count = 0
# #             # 移动到指定位置的前一个位置
# #             while count < (pos - 1):
# #                 count += 1
# #                 cur = cur.next
# #             # 插入节点的链接域，指向指定位置的下一个表元素域
# #             node.next = cur.next
# #             # 指定位置前一个的链接域，断开原有的链接，指向插入节点的表元素域
# #             cur.next = node
# #
# #     def remove(self, item):
# #         """删除节点"""
# #         cur = self._head
# #         pre = None
# #         while cur != None:
# #             # 找到指定元素
# #             if cur.item == item:
# #                 # 如果第一个就是删除的节点
# #                 if not pre:
# #                     # 将头指针指向头节点的后一个节点
# #                     self._head = cur.next
# #                 else:
# #                     # 将删除位置前一个节点的next指向删除位置的后一个节点
# #                     pre.next = cur.next
# #                 break
# #             else:
# #                 # 继续按链表后移节点
# #                 pre = cur
# #                 cur = cur.next
# #
# #     def search(self, item):
# #         """
# #         链表查找节点是否存在，返回True或者False
# #         """
# #         cur = self._head
# #         while cur != None:
# #             if cur.item == item:
# #                 return True
# #             cur = cur.next
# #         return False
# #
# #
# # if __name__ == "__main__":
# #     res = SingleLinkList()
# #     res.add(1)
# #     res.add(2)
# #     res.append(3)
# #     res.insert(2, 4)
# #     print("length:",res.length())
# #     res.travel()
# #     print('----------------------')
# #
# #     print(res.search(3))
# #     print(res.search(5))
# #     res.remove(1)
# #     print("length:",res.length())
# #     res.travel()



class ListNode:
    """创建节点"""
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList:
    def __init__(self):
        self._head = None

    def append(self, item):
        """尾部添加元素"""
        node = ListNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
            node.next = None
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next

            cur.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print('cur.val', cur.val)
        while cur.next != None:
            cur = cur.next
            print('cur.val', cur.val)

class Solution():
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 创建新链表
        newnode = SingleLinkList()
        cur1 = l1._head
        cur2 = l2._head
        while (cur1 != None) and (cur2 != None):
            if cur1.val < cur2.val:
                newnode.append(cur1.val)
                cur1 = cur1.next
            elif cur1.val > cur2.val:
                newnode.append(cur2.val)
                cur2 = cur2.next
            else:
                newnode.append(cur1.val)
                newnode.append(cur2.val)
                cur1 = cur1.next
                cur2 = cur2.next
        else:
            if cur1 == None:
                while cur2 != None:
                    newnode.append(cur2.val)
                    cur2 = cur2.next

            elif cur2 == None:
                while cur1 != None:
                    newnode.append(cur1.val)
                    cur1 = cur1.next

        return newnode


if __name__ == "__main__":
    sl1 = SingleLinkList()
    sl1.append(2)
    sl1.append(6)
    sl1.append(9)
    sl1.append(14)
    sl1.append(36)

    sl2 = SingleLinkList()
    sl2.append(3)
    sl2.append(8)
    sl2.append(9)
    sl2.append(12)
    sl2.append(22)
    sl2.append(35)

    # 调用函数，result接收返回值
    res = Solution()
    result = res.mergeTwoLists(sl1, sl2)
    # 遍历验证
    result.travel()