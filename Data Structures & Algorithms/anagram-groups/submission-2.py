class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for i in strs:
            d1 = [0]*26
            for j in i:
                d1[ord(j) - ord("a")] += 1

            if freq.get(tuple(d1)) == None:
                freq[tuple(d1)] = [i]
            else:
                freq[tuple(d1)].append(i)

        
        print(freq)



        return list(freq.values())
