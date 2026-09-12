class Solution:
    def reverseVowels(self, s: str) -> str:

        left  = 0
        right = len(s) - 1
        words = list(s)                                                    # Mutable copy
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}    # O(1) lookup

        while left < right:
            if words[left] in vowels and words[right] in vowels:
                words[left], words[right] = words[right], words[left]     # Swap vowels
                left  += 1
                right -= 1
            elif words[left] in vowels:
                right -= 1                   # Right is consonant — move right inward
            elif words[right] in vowels:
                left  += 1                   # Left is consonant — move left inward
            else:
                left  += 1                   # Both consonants — skip both
                right -= 1

        return "".join(words)
