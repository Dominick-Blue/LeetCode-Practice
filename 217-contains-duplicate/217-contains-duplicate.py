class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = Counter(nums)
        
        for num in nums:
            if dict[num] >= 2:
                return True
        return False