class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        i=j=x=0
        while j < len(word):
            if word[j] in ['a', 'e', 'i', 'o', 'u'] and (word[j-1] <= word[j] or j == 0):
                j += 1
            else:
                if len(set(word[i:j])) == 5:
                    x = max(x,j-i)
                i = j
                j += 1
        if len(set(word[i:j])) == 5:
            x = max(x,j-i)
        return x