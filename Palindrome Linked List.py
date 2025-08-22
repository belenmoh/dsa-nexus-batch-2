class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        num = head
        while num:
            stack.append(num.val)
            num = num.next
        num2 = head
        for i in range(len(stack)):
            if stack.pop() != num2.val:
                return False
            num2 = num2.next
        return True
