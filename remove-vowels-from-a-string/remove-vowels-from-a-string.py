class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = []
        for i in list(s):
            if i not in vowels:
                ans.append(i)
        return "".join(ans)