import logging

class Solution:
    logging.basicConfig(level=logging.DEBUG)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mymap = defaultdict(int)

        for ind, val in enumerate(s):
            s_val = val
            t_val = t[ind]

            mymap[s_val] += 1
            mymap[t_val] -= 1

        for character, count in mymap.items():
            if count != 0:
                return False
        
        return True

