class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
 
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT
    
    # O(n) time, both strings are the same length (n).
    # O(1) memory, if the character set is fixed,
    # worst case with a large or variable character set, it could be O(n) space.