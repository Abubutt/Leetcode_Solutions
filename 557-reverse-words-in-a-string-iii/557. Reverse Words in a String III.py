class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        reverseWords = []

        for word in words:
            reverseWord = []
            for i in range(len(word) - 1, -1, -1):
                reverseWord.append(word[i])
            
            reverseWords.append("".join(reverseWord))

        return " ".join(reverseWords)




        