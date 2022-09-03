class Solution:
    def printSequence(self,S):
        data = [
        '2', '22','222',
        '3','33', '333',
        '4', '44','444',
        '5', '55', '555',
        '6', '66', '666', 
        '7', '77', '777', '7777',
        '8', '88', '888',
        '9', '99', '999', '9999']
        
        res = ''
        for i in range(len(S)):
            if S[i] == ' ':
                res= res+ '0'
            else:
                index = ord(S[i])-ord('A')
                res = res + data[index]
        return res
        



s = Solution()
print(s.printSequence('GFG')) #43334