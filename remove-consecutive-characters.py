class Solution:
    def removeConsecutiveCharacter(self, S):
        ans = ''
        for i in range(len(S)):
            if i == len(S)-1:
                ans = ans+S[i]
                break
            elif S[i] != S[i+1]:
                 ans += S[i]
        return ans
s = Solution()
print(s.removeConsecutiveCharacter('aabb'))