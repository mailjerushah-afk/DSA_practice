class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None:
            return []
        
        num = len(nums)
        res = [1] * num

        left = 1
        right = 1
        for i in range(num):
            res[i] = left
            left *= nums[i]

        for i in range(num-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res        
