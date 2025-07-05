class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        rev_z = z[::-1]
        ans = (z == rev_z)
        return ans
