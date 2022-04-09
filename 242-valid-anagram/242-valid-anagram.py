class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        for a in set(s):
            if s.count(a) != t.count(a):
                return False
        return True
