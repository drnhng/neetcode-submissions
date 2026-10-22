class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq=[]
        mydict = defaultdict(int)
        for ind, val in enumerate(nums):
            mydict[val] += 1

        for key, val in mydict.items():
            heapq.heappush(pq, (val*-1, key))
        ans = []
        while k > 0:
            ans.append(heapq.heappop(pq)[1])
            k -=1
        return ans