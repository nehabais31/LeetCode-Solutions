class Solution:
    def findReplaceString(self, S, indexes, sources, targets) :
        modified = list(S)
        for idx, src, tgt in zip(indexes, sources, targets):
            if S.startswith(src, idx):
                modified[idx] = tgt
                for i in range(idx+1, len(src)+idx):
                 modified[i] = ''
        return ''.join(modified)
    
sol = Solution()
S1 = "abcd"
indexes1 = [0, 2]
sources1 = ["a", "cd"]
targets1 = ["eee", "ffff"]
print(sol.findReplaceString(S1, indexes1, sources1, targets1))   

S2 = "abcd"
indexes2 = [0, 2]
sources2 = ["ab","ec"]
targets2 = ["eee","ffff"] 
print(sol.findReplaceString(S2, indexes2, sources2, targets2))   
