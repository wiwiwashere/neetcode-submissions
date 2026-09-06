class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # you want higher profit and less capital
        # the more capital u have the more projects u could do
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        queue = []
        indexAvailableTil = 0
        if projects[0][0] > w:
            return w
        for i in range(k):
            # at most k selections
            while indexAvailableTil < n and projects[indexAvailableTil][0] <= w:
                heapq.heappush(queue, -projects[indexAvailableTil][1])
                print(projects[indexAvailableTil][1])
                indexAvailableTil += 1
            w += -heapq.heappop(queue)
        return w
