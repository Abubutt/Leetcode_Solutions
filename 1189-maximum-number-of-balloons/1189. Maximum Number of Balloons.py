from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        wordFreq = {'b': 1, 'a': 1, 'l':2, 'o': 2, 'n': 1}
        freq = defaultdict(int)
        
        for char in text:
            freq[char] += 1
            
        possibleAmount = float('inf')
        
        for char in wordFreq:
            curr = freq[char] // wordFreq[char]
            possibleAmount = min(possibleAmount, curr)
        
        return possibleAmount
            
        
        