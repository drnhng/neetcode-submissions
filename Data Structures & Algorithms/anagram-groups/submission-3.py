class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)

        for a in strs:
            my_list = [0] * 26
            for word in a:
                for c in word:
                    my_list[ord(c)-ord('a')] += 1
            my_map[tuple(my_list)].append(a)

        return list(my_map.values())
