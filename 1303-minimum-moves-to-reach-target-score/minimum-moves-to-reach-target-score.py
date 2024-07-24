class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        #(10-1-1)/4 - 1 = 1 -->moves would be 4
        # (((19-1)2 - 1) / 2) - 1 - 1 - 1 = 1 --> moves would be 7
        # 5-1-1-1-1 = 1 --> moves would be 4
        res = 0
        while target > 1:
            if target % 2 == 0:
                if maxDoubles == 0:
                    res += (target - 1)
                    break
                if maxDoubles > 0:
                    target //= 2
                    res += 1
                    maxDoubles -= 1
            elif target % 2 == 1:
                if maxDoubles == 0:
                    res += (target - 1)
                    break
                target -= 1
                res += 1
        return res
        # debugging
        """
        19 > 1 --> elif --> 18,1
        forgot to decrement maxDoubles
        10 > 1 --> if --> 5,1,3 --> elif --> 4,2,3 --> if --> 2,3,2 --> 1,4,1

        """