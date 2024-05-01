class Solution:
    def similarPairs(self, words: List[str]) -> int:
        arr=[]
        similar_pairs=0
        for word in words:
            dict={}
            for char in word:
                if char in dict:
                    continue
                else:
                    dict[char]=1
            arr.append(dict)

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                    similar_pairs+=1
        return similar_pairs
