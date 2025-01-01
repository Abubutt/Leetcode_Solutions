class MinStack:

    def __init__(self):
        self.minStack = []
        self.minVal = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal, val)
        self.minStack.append(self.minVal)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            self.stack.pop()
        if not self.stack:
            self.minVal = float('inf')
        else:
            self.minVal = self.minStack[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()