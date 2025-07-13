class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        ans = []
        while i>=0:
            if s[i] == "#":
                num = int(s[i-2:i])
                let_1 = 97 + num - 1
                char = chr(let_1)
                ans.append(char)
                i -= 3
            else:
                num = int(s[i])
                let_1 = 97 + num - 1
                char = chr(let_1)
                ans.append(char)
                i -= 1
        return "".join(ans[::-1])
