class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass_change = [0] * 1001

        for t in trips:
            num_pass, start, end = t
            pass_change[start] += num_pass
            pass_change[end] -= num_pass

        cur_pass = 0
        for i in range(1001):
            cur_pass += pass_change[i]
            if cur_pass > capacity:
                return False
        return True