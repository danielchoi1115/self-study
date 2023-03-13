class Solution:
    def myAtoi(self, s: str) -> int:
        signs = {'-','+'}
        numbers = {'0','1','2','3','4','5','6','7','8','9'}
        s = s.strip()
        i = 0
        num = ""
        while i < len(s):
            if s[i] in signs and not num:
                num += s[i]
            elif s[i] in numbers:
                num += s[i]
            else:
                break
            i += 1
        s = s[:i].strip()
        num = 0 if s in signs or s == "" else int(s)
        num = max(num, -pow(2, 31))
        return min(num, pow(2, 31)-1)
    
s = Solution()
print(s.myAtoi("   -42"))