class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(tasks)
        processorTime.sort()
        tasks.sort()
        j = n - 1
        m = len(processorTime)
        ans = 0
        for i in range(m):
            c = 0
            while c < 4:
                ans = max(ans, processorTime[i] + tasks[j])
                c += 1
                j -= 1
        return ans