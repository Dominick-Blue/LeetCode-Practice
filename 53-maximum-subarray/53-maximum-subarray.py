class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP
        # T: O(N)
        # S: O(N)
        
        cache = [0] * len(nums)
        cache[0] = nums[0]
        
        for i in range(1, len(nums)):
            cache[i] = max(nums[i] + cache[i-1], nums[i])
            
        return max(cache)
        