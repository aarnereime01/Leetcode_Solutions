class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ''

        import math

        gcd = math.gcd(len(str1), len(str2))
        return str1[:gcd]
    
if __name__ == '__main__':
    str1 = 'ABCABC'
    str2 = 'ABC'
    
    print(Solution().gcdOfStrings(str1, str2)) # Output: 'ABC'
    