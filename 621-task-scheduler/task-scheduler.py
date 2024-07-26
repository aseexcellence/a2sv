from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-f for f in count.values()]
        print(maxHeap)
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                freq = 1 + heapq.heappop(maxHeap)
                if freq:
                    q.append([freq, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        
        return time