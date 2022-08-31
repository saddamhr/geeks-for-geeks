class Solution:
    def findSum(self,A,N):
        min_number, max_number = A[0], A[0]
        for element in A:
            if element < min_number:
                min_number = element
            elif element > max_number:
                max_number = element
        return min_number+ max_number

s = Solution()
s.findSum([-2, 1, -4, 5, 3], 5)