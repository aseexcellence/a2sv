class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.tripTimeMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInMap.pop(id)
        if(startStation, stationName) not in self.tripTimeMap:
            self.tripTimeMap[(startStation, stationName)] = []
        self.tripTimeMap[(startStation, stationName)].append(t - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tripTimes = self.tripTimeMap[(startStation, endStation)]
        return sum(tripTimes) / len(tripTimes)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)