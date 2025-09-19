class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        visited = {(0, 0)}
        position = (0, 0)

        for p in path:
            x, y = direction[p]
            posX, posY = position
            newPos = (posX + x, posY + y)
            
            if newPos in visited:
                return True
            
            visited.add(newPos)
            position = newPos

        return False
        