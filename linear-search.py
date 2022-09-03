class Solution:
    def linear_search(self, A : list, key : int):
        for i in range(len(A)):
            if A[i] == key:
                return i
        return -1

s = Solution()
print(s.linear_search([5, 6, 7, 8, 9, 10, 1, 2, 3], 10))