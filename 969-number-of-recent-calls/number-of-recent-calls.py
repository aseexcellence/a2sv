class RecentCounter:

    def __init__(self):
        self.recreq = deque()

    def ping(self, t: int) -> int:
        self.recreq.append(t)
        while self.recreq[0] < t - 3000:
            self.recreq.popleft()
        return len(self.recreq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)