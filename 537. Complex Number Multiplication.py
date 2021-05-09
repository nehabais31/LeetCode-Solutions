class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # (a + bi) * (x + iy) = (ax - by) + i(ay + bx)

        num1_list = num1.split('+')
        num2_list = num2.split('+')

        real1 = num1_list[0]
        img1  = num1_list[1][ : num1_list[1].find('i')]

        real2 = num2_list[0]
        img2  = num2_list[1][ : num2_list[1].find('i')]

        res = str(int(real1) * int(real2) - int(img1) * int(img2) ) + '+' + \
              str(int(real1) * int(img2) + int(real2) * int(img1) ) + 'i'

        return res
    
sol = Solution()
print(sol.complexNumberMultiply("1+1i", "1+1i"))
print(sol.complexNumberMultiply("1+-1i", "1+-1i"))