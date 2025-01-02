from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.size += 1

        for i in range(self.size - 1):
            self.queue2.append(self.queue1.popleft())
        
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        if self.queue1:
            self.size -= 1
            return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]
        

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()