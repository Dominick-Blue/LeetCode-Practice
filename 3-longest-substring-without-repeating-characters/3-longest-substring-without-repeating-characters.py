class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_map = {}
        left, result = 0,0
        
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(char_map[s[right]], left)
            
            result = max(result, right - left + 1)
            char_map[s[right]] = right + 1
        return result