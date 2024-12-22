class Solution:
    def isPathCrossing(self, path: str) -> bool:
        movement = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        visited = {(0, 0)}
        pos = (0, 0)

        for move in path:
            dx, dy = movement[move]
            x, y = pos
            pos = (x+dx, y+dy)

            if pos in visited:
                return True
            visited.add(pos)
        
        return False
            

        