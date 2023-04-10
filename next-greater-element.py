'''
Solution 01:
Time and space: 0(n^2) and 0(1)
Status: TLE
'''
class Solution:
    def nextLargerElement(self,arr,n):
        res = []
        for i in range(n-1):
            largest_val = -1
            for j in range(i+1, n):
                if arr[i] < arr[j]:
                    largest_val = arr[j]
                    break
            res.append(largest_val)
        res.append(-1)
        return res
'''
Solution 02:
Time and space: 0(n) and 0(n)
Status: Accepted
'''
class Solution:
    def nextLargerElement(self,arr,n):
        stack = list()
        result = []
        for i in range(n - 1, -1, -1):
            if len(stack) == 0:
                result.append(-1)
            else:
                top = stack[0]
                if top > arr[i]:
                    result.append(top)
                else:
                    while len(stack) != 0 and stack[0] <= arr[i]:
                        stack.pop(0)
                    if len(stack) == 0:
                        result.append(-1)
                    else:
                        result.append(stack[0])
            stack.insert(0, arr[i])
        return result[::-1]