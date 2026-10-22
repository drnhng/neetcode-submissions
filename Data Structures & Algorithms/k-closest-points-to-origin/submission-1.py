class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        heapq.heapify(pq)
        for i, a in enumerate(points):
            dist = math.sqrt(a[1]*a[1] + a[0]*a[0])
            tup = [dist, a]
            heapq.heappush(pq, tup)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(pq)[1])
            k-=1
        return ans