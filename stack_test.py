# class Stack:
#     def __init__(self):
#         self.MaxSize = 10
#         self.head = [None for x in range(self.MaxSize)]
#         self.top = -1
#
#     def is_empty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False
#
#     def add_data(self, data):
#         if self.top < self.MaxSize - 1:
#             self.top += 1
#             self.head[self.top] = data
#         else:
#             print('栈满')
#             return
#
#     def out_data(self):
#         if self.is_empty():
#             print('栈空')
#         else:
#             out_elem = self.top
#             self.top -= 1
#             return self.head[out_elem]
#
#     def tarvers(self):
#         if not self.is_empty():
#             for num in range(self.top, -1, -1):
#                 print(self.head[num])
#
#     def get_top(self):
#         if self.is_empty():
#             return '空'
#         else:
#             return self.head[self.top]
#
#     def get_length(self):
#         if self.is_empty():
#             return 0
#         else:
#             return self.top + 1
#
#     def visit_memb(self, num):
#         if num < self.MaxSize:
#             return self.head[num]
#
#
# def huiwen(strs):
#     stack = Stack()
#     for elem in strs:
#         stack.add_data(elem)
#     for num in range(stack.get_length()):
#         out_elem = stack.out_data()
#         if strs[num] != out_elem:
#             print('不是回文')
#             break
#     else:
#         print('是回文')
#
#
# def kuohao(kuo):
#     stack = Stack()
#     rev = {'{': '}', '(': ')', '<': '>'}
#     for elem in kuo:
#         if elem in ['{', '(', '<']:
#             stack.add_data(elem)
#         else:
#             top_elem = stack.get_top()
#             if rev[top_elem] != elem:
#                 # print('不匹配')
#                 break
#             else:
#                 stack.out_data()
#
#     if stack.is_empty():
#         print('匹配')
#     else:
#         print('不匹配',stack.get_top())
#
#
# if __name__ == "__main__":
#     # print('1111111111111')
#     # test = Stack()
#     # print(test.is_empty())
#     # test.add_data(5)
#     # test.tarvers()
#     # print('-----------1------------')
#     # test.add_data(7)
#     # test.tarvers()
#     # test.add_data(9)
#     # test.tarvers()
#     # print('-----------2------------')
#     #
#     # print(test.out_data())
#     # print('------------3---------')
#     # test.tarvers()
#     # print('------------4-----------')
#     # print(test.get_top())
#     #
#     # print(test.get_length())
#     # print('----------5---------')
#     # print(test.visit_memb(1))
#     # str = 'qwertrewq'
#     # huiwen(str)
#     str2 = '(){<>}<><>'
#     kuohao(str2)


class Stack:
    def __init__(self):
        self.stack = list()
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push_elem(self, data):
        self.top += 1
        self.stack.append(data)

    def pop_elem(self):

        self.top -= 1
        res = self.stack.pop()
        return res

    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[self.top]


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        str_dict = {'(': ')', '{': '}', '[': ']'}
        if not s:
            return False
        if s[0] in [')', '}', ']']:
            return False
        for elem in s:
            if elem in ['(', '{', '[']:
                stack.push_elem(elem)
            else:
                if stack.is_empty():
                    return False

                top_elem = stack.get_top()
                if str_dict[top_elem] != elem:
                    break
                else:
                    pop = stack.pop_elem()
                    print('弹出', pop)

        if stack.is_empty():
            return True
        else:
            return False


tt = Solution()
strs = "()[]{}"
print(tt.isValid(strs))