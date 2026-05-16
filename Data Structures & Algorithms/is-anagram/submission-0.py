class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if d1.get(s[i]) == None:
                d1[s[i]] = 1
            else:
                d1[s[i]] += 1

            if d2.get(t[i]) == None:
                d2[t[i]] = 1
            else:
                d2[t[i]] += 1

        for k, v in d1.items():
            if d2.get(k) == None:
                return False
                
            if d2[k] != v:
                return False

        return True

        