class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            if not stack:
                stack.append(temperatures[i])
                continue
            ct = 1
            restoreStack = []
            while stack and stack[-1] <= temperatures[i]:
                restoreStack.append(stack.pop())
                ct +=1
            if not stack:
                ans[i] = 0
            else:
                ans[i] = ct
            while restoreStack:
                stack.append(restoreStack.pop())
            stack.append(temperatures[i])
        return ans