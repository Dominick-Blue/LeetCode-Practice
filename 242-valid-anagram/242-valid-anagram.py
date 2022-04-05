class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        count_s, count_t = {},{}
        
        for i in range(0, len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        for char in count_s:
                if count_s[char] != count_t.get(char, 0):
                    return False
                
        return True
                