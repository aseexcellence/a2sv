class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph, incoming edges
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        # find source nodes
        queue = deque([])
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)

        ordered = []
        # BFS
        while queue:
            child = queue.popleft()
            ordered.append(child)

            for dependent in graph[child]:
                incoming[dependent] -= 1
                if incoming[dependent] == 0:
                    queue.append(dependent)

        return ordered if len(ordered) == numCourses else []