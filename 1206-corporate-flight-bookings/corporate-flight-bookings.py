class Solution(object):
    def corpFlightBookings(self, bookings, n):
        answer = [0] * (n + 1)
        
        for first, last, seats in bookings:
            answer[first - 1] += seats
            if last < n:
                answer[last] -= seats

        # Compute prefix sum
        for i in range(1, n):
            answer[i] += answer[i - 1]

        return answer[:n]

