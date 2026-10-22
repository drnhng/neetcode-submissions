class Solution:
    def isPermutation(self, s1: str, s2:str, char_counts: list[int]) -> bool:
        if len(s1) != len(s2):
            return False
        for char in s2:
            char_counts[ord(char)] -= 1
            if char_counts[ord(char)] < 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_counts = [0] * 256
        for char in s1:
            char_counts[ord(char)] += 1
        l = 0
        for r, a in enumerate(s2):
            char_counts[ord(a)] -= 1
            while char_counts[ord(a)] < 0:
                char_counts[ord(s2[l])] += 1
                l += 1
            if sum(char_counts) == 0:
                return True
        return False
            