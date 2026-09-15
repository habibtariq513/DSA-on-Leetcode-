class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w = list(word)
        if ch not in w:
            return word

        i = 0
        j = w.index(ch)

        while i < j:
            w[i], w[j] = w[j], w[i]
            i += 1
            j -= 1

        return ''.join(w)
