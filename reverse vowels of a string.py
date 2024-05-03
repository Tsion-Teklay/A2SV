class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        n = len(s)
        f = 0
        e = n - 1

        while f < e:
            if s[f] not in vowels:
                f += 1
            elif s[e] not in vowels:
                e -= 1
            else:
                s[f], s[e] = s[e], s[f]
                f += 1
                e -= 1

        return ''.join(s)
