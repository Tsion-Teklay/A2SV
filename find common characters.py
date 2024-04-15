class Solution(object):
    def commonChars(self, words):
        result = []
        count = {}

        for char in words[0]:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for word in words[1:]:
            temp = {}
            for char in word:
                if char in temp:
                    temp[char] += 1
                else:
                    temp[char] = 1

            for char in count:
                if char in temp:
                    count[char] = min(count[char], temp[char])
                else:
                    count[char] = 0

        for char, freq in count.items():
            result.extend([char] * freq)

        return result
