from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.queueSize = 0
        self.size = size
        self.movingSum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.movingSum += val
        self.queueSize += 1
        
        while self.queueSize > self.size:
            self.movingSum -= self.queue.popleft()
            self.queueSize -= 1
        
        
        return self.movingSum / min(self.queueSize, self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)