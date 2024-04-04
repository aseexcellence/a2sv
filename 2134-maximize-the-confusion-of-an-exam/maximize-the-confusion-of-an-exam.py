class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''keep count of # of T's and F's found in z 2 pointers window
        if both count of T and F > k then, reduce count at left and
        inc left until either count of T or F <= k
        at each iternation find the max window length'''

        cntT, cntF, left = 0, 0, 0
        maxT_or_F = 1
        for i in range(len(answerKey)):
            if answerKey[i] == 'T':
                cntT += 1
            else:
                cntF += 1
            
            while min(cntT, cntF) > k:
                if answerKey[left] == 'T':
                    cntT -= 1
                else:
                    cntF -= 1
                
                left += 1
            maxT_or_F = max(maxT_or_F, i - left + 1)
        
        return maxT_or_F
