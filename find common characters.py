class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        duplicates = []
        result = Counter(words[0])
        for word in words[1:]:
            result &= Counter(word)
        for char, count in result.items():
            duplicates.extend([char]*count)
        return duplicates
