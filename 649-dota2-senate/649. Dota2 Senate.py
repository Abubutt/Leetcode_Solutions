class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque()
        rq = deque()
        count = len(senate)

        for i in range(count):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)

        while dq and rq:
            count += 1
            
            if dq[0] < rq[0]:
                dq.append(count)
            else:
                rq.append(count)

            rq.popleft()
            dq.popleft()

        if dq:
            return "Dire"
        
        return "Radiant"

        