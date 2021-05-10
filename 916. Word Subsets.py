'''
We are given two arrays A and B of words.  Each word is a string of lowercase letters.
For example, "wrr" is a subset of "warrior", but is not a subset of "world".
Now say a word a from A is universal if for every b in B, b is a subset of a. 
Return a list of all universal words in A.  You can return the words in any order
'''

class Solution:
    def wordSubsets(self, A, B):
        import collections
        count = collections.Counter()
        for word in B:
            count |= collections.Counter(word)  # union |= -> to merge results for each word
            
        res = []
        for word in A:
            if not count - collections.Counter(word):
                res.append(word)
                
        return res

sol = Solution() 
A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","oo"]
print(sol.wordSubsets( A, B))