class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={num: i for i, num in enumerate(nums)}
        
        for i in range(len(nums)):
            if target-nums[i] in d and i!=d[target-nums[i]]:
                return [i, d[target-nums[i]]]