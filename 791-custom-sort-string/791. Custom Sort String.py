class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = []
        ordering = [[] for i in range(len(order))]
        pos = {}

        for i in range(len(order)):
            pos[order[i]] = i

        for char in s:
            if char in pos:
                ordering[pos[char]].append(char)
            else:
                ordering.append([char])

        for val in ordering:
            if len(val) > 0:
                ans.extend(val)

        return "".join(ans)

        