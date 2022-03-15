from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         count = {}
        
#         for index,num in enumerate(nums):
#             complement = target - num
#             if complement in count:
#                 return [index, count[complement]]
#             count[num] = index
        
        count = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in count:
                return [index, count[complement]]
            count[num] = index