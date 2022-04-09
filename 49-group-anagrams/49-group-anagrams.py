class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Create a dictionary using defaultdict
        # Assign sorted strings to dictionary on pass 1
        # Compare strings in str on pass 2 and if they match a key in the dictionary, append result
        # Return result
        
        key_map = defaultdict(list)
        
        for s in strs:
            key_map["".join(sorted(s))].append(s)
        
        return key_map.values()
            