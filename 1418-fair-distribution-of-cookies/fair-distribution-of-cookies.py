class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(p):
            nonlocal best
            if p == len(cookies):
                best = min(best, max(split))
                return
            
            if len(split) < k:
                split.append(cookies[p])
                backtrack(p + 1)
                split.pop()

            seen = set()
            for i in range(len(split)):
                if split[i] + cookies[p] < best and split[i] not in seen:
                    seen.add(split[i])
                    split[i] += cookies[p]
                    backtrack(p + 1)
                    split[i] -= cookies[p]
        
        split = []
        best = float("inf")
        backtrack(0)
        return best