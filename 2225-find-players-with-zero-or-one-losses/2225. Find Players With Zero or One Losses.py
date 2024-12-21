from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        stats = {}
        
        for match in matches:
            winner, loser = match
            if winner not in stats:
                stats[winner] = {"win": 1, "lose": 0}
            if loser not in stats:
                stats[loser] = {"win": 0, "lose": 1}
                continue
                
            if winner in stats:
                stats[winner]["win"] += 1
            if loser in stats:
                stats[loser]["lose"] += 1
        
            
        noLost = []
        oneLost = []
        for stat, val in stats.items():
            if val["lose"] == 0:
                noLost.append(stat)
            elif val["lose"] == 1:
                oneLost.append(stat)
        
        noLost.sort()
        oneLost.sort()
        
        return [noLost, oneLost]
                
            
        