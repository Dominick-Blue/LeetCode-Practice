class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP Approach - Kadane's Algorithm
        # Time Complexity: O(n) & Space Complexity: O(1)
        
        current_sub = nums[0]
        max_sub = nums[0]
        
        for num in nums[1:]:
            current_sub = max(num, current_sub + num)
            max_sub = max(max_sub, current_sub)
        return max_sub