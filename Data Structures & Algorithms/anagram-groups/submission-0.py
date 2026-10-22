class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for ind, val in enumerate(strs):
            sorted_val = "".join(sorted(val))
            mydict[sorted_val].append(val)
        ans = []
        for key, val in mydict.items():
            ans.append(val)
        return ans