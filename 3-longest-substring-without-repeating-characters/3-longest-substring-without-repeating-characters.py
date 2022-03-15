class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_len = len(s)
        max_len = 0
        
        char_map = {}
        
        window_start = 0
        
        for window_end in range(list_len):
            if s[window_end] in char_map:
                window_start = max(char_map[s[window_end]], window_start)
            
            max_len = max(max_len, window_end - window_start + 1)
            char_map[s[window_end]] = window_end + 1
            
        return max_len