class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        list_length = len(s)
        max_subarray = 0
        window_start = 0
        char_map = {}
        
        for window_end in range(list_length):
            if s[window_end] in char_map:
                window_start = max(char_map[s[window_end]], window_start)
                
            max_subarray = max(max_subarray, window_end - window_start + 1)
            char_map[s[window_end]] = window_end + 1
        return max_subarray