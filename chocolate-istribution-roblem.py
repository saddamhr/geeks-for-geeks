class Solution:
    def findMinDiff(self, arr, s):
        arr.sort()
        min_diff = arr[len(arr)-1] - arr[0]
        # print(range(len(arr)-s+1))
        for i in range(len(arr)-s+1):
            print(i)
            min_diff = min(min_diff, arr[i+s-1]-arr[i])
        return min_diff


s = Solution()
print(s.findMinDiff([3, 4, 1, 9, 56, 7, 9, 12], 5))