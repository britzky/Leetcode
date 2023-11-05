class Solution(object):
    def getWinner(self, arr, k):
        max_element = max(arr)
        queue = deque(arr[1:])
        current = arr[0]
        winstreak = 0

        while queue:
            opponent = queue.popleft()
            if current > opponent:
                queue.append(opponent)
                winstreak += 1
            else:
                queue.append(current)
                current = opponent
                winstreak = 1

            if winstreak == k or current == max_element:
                return current 

        