class Solution(object):
    def longestCommonPrefix(self, strs):
        res = "" 

        for i in range(len(strs[0])): # loopinam per kiekviena pirmojo string'o raide
            for s in strs: # loopinam per kiekviena zodi masyve
                # jei pasiekiame zodzio gala, arba raides nebesutampoa - grazinam rezultata
                if i == len(s) or s[i] != strs[0][i]: 
                    return res
            res += strs[0][i] # jei visi zodziai turi ta pati raidziu prefix'a

        return res
        