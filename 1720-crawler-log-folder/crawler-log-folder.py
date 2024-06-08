class Solution:
    def minOperations(self, logs: List[str]) -> int:
        _cd_in = []
        for log in logs:
            if log == './': continue
            elif log == '../' and not _cd_in: continue
            elif log == '../' and _cd_in: _cd_in.pop()
            else: _cd_in.append(log)
        return len(_cd_in)