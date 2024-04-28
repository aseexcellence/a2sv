class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        processorIndex = 0
        answer = 0

        for processingTime in processorTime:
            currentMax = 0
            taskCount = 0

            while processorIndex < len(tasks) and taskCount < 4:
                currentMax = max(currentMax, processingTime + tasks[processorIndex])
                processorIndex += 1
                taskCount += 1

            answer = max(answer, currentMax)

        return answer