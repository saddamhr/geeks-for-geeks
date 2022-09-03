class Solution:
    def reverseArr(self, arr):
        start, end = 0, len(arr)-1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
        return arr

s = Solution()
print(s.reverseArr([4, 5, 1, 2]))