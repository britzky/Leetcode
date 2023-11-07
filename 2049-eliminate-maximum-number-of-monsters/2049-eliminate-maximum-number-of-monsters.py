from math import ceil

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        # Calculate arrival times
        arrival_times = []
        for i in range(len(dist)):
            arrival_time = ceil(dist[i] / float(speed[i]))
            arrival_times.append(arrival_time)
        
        # Sort arrival times
        arrival_times.sort()
        
        # Iterate and check if we can eliminate all monsters
        for i in range(len(arrival_times)):
            # If arrival time is less than or equal to the time (i)
            # it means a monster reaches the player and cannot be eliminated
            if arrival_times[i] <= i:
                return i
        
        # If all monsters can be eliminated
        return len(dist)
