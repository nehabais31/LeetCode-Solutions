class Solution:
    def mergeAlternately(self, word1, word2) :
        result = ''
        # i = 0
        # while i < len(word1) and i < len(word2):
        #     result += word1[i] + word2[i]

        #     i+= 1

        # if i < len(word1):
        #     result += word1[i:]
        # elif i < len(word2):
        #     result += word2[i:]

        # return result
        
        for i in range(min(len(word1), len(word2))):
            result += word1[i] + word2[i]
            
        return result + word1[i+1: ] + word2[i+1: ]
    
sol = Solution()
print(sol.mergeAlternately('neha', 'dipen'))