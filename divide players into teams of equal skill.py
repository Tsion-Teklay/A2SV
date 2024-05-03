class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        p1 = 0
        p2 = n - 1
        s = 0

        m = skill[p1] + skill[p2]

        while p1 < p2:
            if skill[p1] + skill[p2] != m:
                return -1
            else:
                s += skill[p1] * skill[p2]
                p1 += 1
                p2 -= 1
        return s
