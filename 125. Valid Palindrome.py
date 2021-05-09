class Solution:
    def isPalindrome(self, s: str) -> bool:
        # import re
        # s_nopunc = re.sub(r'[^\w\s]', '', s)
        # s_list = s_nopunc.split()
        
        # res_string = ''
        # for word in s_list:
        #     if word.isalnum():
        #         res_string += word.lower()
        
        # return res_string == res_string[::-1]
        
        res_string = ''
        for word in s:
            if word.isalnum():
                res_string += word.lower()
                
        return res_string == res_string[::-1]

                
    
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))