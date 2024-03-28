class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        losses = defaultdict(int)

        for winner, loser in matches:
            wins[winner] += 1
            losses[loser] += 1
        
        zero_losses = [player for player in wins if player not in losses]
        one_loss = [player for player, loss_count in losses.items() if loss_count == 1]

        return [sorted(zero_losses), sorted(one_loss)]