class Solution:
    def binary_serach(self, A:list, key: int):
        A.sort()
        left, right = 0, len(A)-1
        while left <= right:
            mid = (left + right) //2
            if A[mid] == key:
                return mid
            elif A[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        return -1

s = Solution()
print(s.linear_search([5, 6, 7, 8, 9, 10, 1, 2, 3], 10))