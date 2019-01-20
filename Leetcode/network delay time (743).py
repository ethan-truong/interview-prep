class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        children = {}
        weights = {}

        for i in range(1, N + 1):
            children[i] = []
            weights[i] = sys.maxint

        for time in times:
            children[time[0]].append([time[1], time[2]])

        queue = [K]
        weights[K] = 0
        visited = []

        def visit(node):
            visited.append(node)
            for child in children[node]:
                if child[0] not in visited:
                    queue.append(child[0])
                if weights[node] + child[1] < weights[child[0]]:
                    weights[child[0]] = weights[node] + child[1]
                    queue.append(child[0])

        while len(queue) > 0:
            visit(queue.pop(0))

        for i in range(1, N + 1):
            if i not in visited:
                return -1

        return max(weights.values())




