"""
66. Plus One

Given a non-empty array of decimal digits representing a non-negative integer, 
increment one to the integer.

The digits are stored such that the most significant digit 
is at the head of the list, 
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, 
except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits):

        digits[-1] += 1
        
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            else:
                digits[i] = 0
                digits[i - 1] += 1
                
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        
        return digits      
    

# Driver code
digits = [9,9,9]
sol = Solution()
print(sol.plusOne(digits))