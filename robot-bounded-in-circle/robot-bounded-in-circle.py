class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        origin = [0,0]
        direction = 0 # N=0, E=1, S=2, W=3
        # there's four directions, 4 loops are sufficient for robot to return initial state
        instructions = instructions*4
        
        # run the instructions
        for ins in instructions:
            if ins == 'G':
                if direction == 0: origin[0]+=1
                if direction == 1: origin[1]+=1
                if direction == 2: origin[0]-=1
                if direction == 3: origin[1]-=1
            elif ins == 'L':
                if direction == 0: direction = 3
                else: direction -= 1
            elif ins == 'R':
                if direction == 3: direction = 0
                else: direction +=1 
                    
        # determine if it is at (0,0) and pointing north
        return origin == [0,0] and direction == 0
        