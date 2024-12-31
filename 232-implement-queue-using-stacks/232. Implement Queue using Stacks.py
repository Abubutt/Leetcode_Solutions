class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.top = None

    def push(self, x: int) -> None:
        if self.stack2:
            self.top = self.stack2[-1]

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)
        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        popElement = self.stack2.pop()
        if self.stack2:
            self.top = self.stack2[-1]
        return popElement
        

    def peek(self) -> int:
        if not self.stack2:
            return self.stack1[0]
        return self.top
        
    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()