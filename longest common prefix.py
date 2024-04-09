class Solution(object):
  def longestCommonPrefix(self,strs):
    if not strs:
        return "" 
    min_length = min(len(s) for s in strs)  
    prefix = ""
    for i in range(min_length):
        char = strs[0][i] 
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return prefix  
        prefix += char  
    return prefix
        
