class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n=len(players)
        m=len(trainers)
        p1=0
        p2=0
        counter=0

        while p1<n and p2<m:
            if players[p1]<=trainers[p2]:
                counter+=1
                p1+=1
                p2+=1
            else:
                p2+=1

        return counter
        
