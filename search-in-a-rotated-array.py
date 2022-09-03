# linear search 
class Solution:
    def linear_search(self, A : list, key : int):
        for i in range(len(A)):
            if A[i] == key:
                return i
        return -1
    # def binary_serach(self, A:list, key: int):
    #     A.sort()
    #     print(A)
    #     left, right = 0, len(A)-1

    #     while left <= right:
    #         mid = (left + right) //2
    #         if A[mid] == key:
    #             return mid
    #         elif A[mid] < key:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return -1

s = Solution()
print(s.linear_search([5, 6, 7, 8, 9, 10, 1, 2, 3], 10))