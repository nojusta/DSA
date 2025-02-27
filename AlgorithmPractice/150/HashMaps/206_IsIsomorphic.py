class Solution(object):
    def isIsomorphic(self, s, t):
        MapST, MapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in MapST and MapST[c1] != c2) or
                (c2 in MapTS and MapTS[c2] != c1)):
                return False

            MapST[c1] = c2
            MapTS[c2] = c1


        return True 
        