class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        l = 0
        r = len(s) - 1
        charList = list(s)

        while l < r:
            while l < r and charList[l] not in vowels:
                l += 1
            while l < r and charList[r] not in vowels:
                r -= 1
            
            if l < r:
                charList[l], charList[r] = charList[r], charList[l]
                l += 1
                r -= 1

        return ''.join(charList)
