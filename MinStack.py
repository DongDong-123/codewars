class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = -1
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # if self.head == -1:
        self.data.append(x)
        self.head += 1

    def pop(self):
        """
        :rtype: void
        """
        elem = self.data.pop()
        self.head -= 1

        return elem

    def top(self):
        """
        :rtype: int
        """
        if self.head == -1:
            return None
        else:
            return self.data[self.head]

    def getMin(self):
        """
        :rtype: int
        """
        if self.head == -1:
            return None
        else:
            index = self.head
            min_elem = self.data[self.head]
            while index >= 0:
                min_elem = min(min_elem, self.data[index])
                index -= 1
            return min_elem

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
# minStack.getMin()
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
# minStack.getMin()