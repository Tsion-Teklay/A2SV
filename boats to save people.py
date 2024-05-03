class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort(reverse=True)
        p1 = 0
        p2 = n - 1
        counter = 0

        while p1 <= p2:
            if people[p1] + people[p2] <= limit:
                p1 += 1  
                p2 -= 1  
                counter += 1
            else:
                p1+=1
                counter+=1

        return counter
