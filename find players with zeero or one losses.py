class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins={}
        losses={}

        for winner, loser in matches:
            wins[winner]= wins.get(winner,0)+1
            losses[loser]=losses.get(loser,0)+1

        no_loss=[]
        one_loss=[]

        for player in set(wins.keys()) | set(losses.keys()):
            if losses.get(player,0)==1:
                one_loss.append(player)
            elif losses.get(player,0)==0:
                no_loss.append(player)

        no_loss.sort()
        one_loss.sort()

        return [no_loss,one_loss]
