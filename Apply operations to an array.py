class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        new_array = []
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                new_array.append(num)
        new_array.extend([0] * zeros)
        return new_array
