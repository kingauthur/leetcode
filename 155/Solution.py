class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.currentMin = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

        if len(self.currentMin) == 0:
            self.currentMin.append(x)
        elif x < self.currentMin[-1]:
            self.currentMin.append(x)
        else:
            self.currentMin.append(self.currentMin[-1])



    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack.pop()
            self.currentMin.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 0

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.currentMin[-1]
        else:
            return 0



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(1)
obj.push(3)
print(obj.pop())
print(obj.top())
print(obj.getMin())
