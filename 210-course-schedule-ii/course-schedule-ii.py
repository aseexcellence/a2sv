class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Solution using Kahn's Algorithm
        Step 1: find all nodes in the graph that have no incoming edges
        Step 2: add the source nodes to the queue
        Step 3: remove the source nodes from the graph
        Step 4: find the source nodes in the reduced graph & repeat the whole process
        '''

        # Step 1: initialization and a for loop to initialize the graph & incoming DS 
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = [] # the return result

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        # Step 2: a for loop to initialize the queue
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        
        # Step 3 & 4: removing the source node, finding the source ndoes from new graph and repeat
        while queue:
            course = queue.popleft()
            order.append(course)

            # iterate through the neighbors in the graph
            for neighbor in graph[course]:
                # decrease the incoming edges for the nighbors
                incoming[neighbor] -= 1
                
                # finding source nodes from the new reduced graph
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        # Why? --> To identify if cycle exists   
        if len(order) != numCourses:
                order = []
        
        return order