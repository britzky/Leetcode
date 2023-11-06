class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.available_seats = [i for i in range(1, n + 1)]

    def reserve(self):
        """
        :rtype: int
        """
        seat_number = heapq.heappop(self.available_seats)
        return seat_number
        

    def unreserve(self, seat_number):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.available_seats, seat_number)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)