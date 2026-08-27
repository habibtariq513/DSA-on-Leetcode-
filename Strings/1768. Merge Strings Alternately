class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w = []
        length = max(len(word1), len(word2))

        w1 = 0
        w2 = 0

        for i in range(0, length):
            if len(word1) > w1:
                w.append(word1[w1])
                w1 += 1
            if len(word2) > w2: 
                w.append(word2[w2])
                w2 += 1

        return ''.join(w)
