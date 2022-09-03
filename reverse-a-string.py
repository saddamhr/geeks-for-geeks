class Solution:
    def reverseWord(self, s):
        str = ''
        for i in s:
            str = i + str
        return str    

s = Solution()
print(s.reverseWord('Geeks'))