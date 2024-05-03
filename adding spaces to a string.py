class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n=len(s)
        m=len(spaces)
        arr=[]
        d=0

        for space in spaces:
            for j in range(space - d):
                arr.append(s[d+j])
            arr.append(' ')
            d = space

        arr.append(s[d:])
        return ''.join(arr)      
