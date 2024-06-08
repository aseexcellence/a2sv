class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        pl, pt = 0, 0
        players.sort()
        trainers.sort()
        res = 0
        while pl < len(players) and pt < len(trainers):
            if players[pl] <= trainers[pt]:
                res += 1
                pl += 1
                pt += 1
            else:
                pt += 1
        
        return res
        