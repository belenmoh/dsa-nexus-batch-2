class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                s1 = set(words[i])
                s2 = set(words[j])
                if s1 == s2:
                    count += 1
        return count
