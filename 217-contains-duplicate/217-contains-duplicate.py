class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        occurence = set()
        
        for num in nums:
            if num in occurence:
                return True
            occurence.add(num)
        return False