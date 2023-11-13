class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0

        max_stop = max(max(route) for route in routes)
        if max_stop < target:
            return -1

        n = len(routes)
        min_busses_to_reach = [float('inf')] * (max_stop + 1)
        min_busses_to_reach[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, min_busses_to_reach[stop])
                mini += 1
                for stop in route:
                    if min_busses_to_reach[stop] > mini:
                        min_busses_to_reach[stop] = mini
                        flag = True
        return min_busses_to_reach[target] if min_busses_to_reach[target] < float('inf') else -1
        