class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.d = 0
        def sums(a, b):
            c = a + b
            if self.d == 1:
                c += 1
                self.d = 0
            if c >= 10:
                c = c-10
                self.d = 1

            return c

        # l1.reverse()
        # l2.reverse()

        res = list(map(sums, l1, l2))
        # res.reverse()
        return res

if __name__ == "__main__":
    a = [2, 4, 3]
    b = [5, 6, 4]
    res = Solution()
    print(res.addTwoNumbers(a, b))

