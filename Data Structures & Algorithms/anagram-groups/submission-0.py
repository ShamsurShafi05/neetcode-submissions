class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = []
        for i in strs:
            d1 = {}
            for j in i:
                if d1.get(j) == None:
                    d1[j] = 1
                else:
                    d1[j] += 1

            freq.append(d1)

        # print(freq)
        
        result = []
        # print()
        # print("Checking:")
        for i in freq:
            # print(i)
            add = []
            for j in range(len(strs)):
                if freq[j] == i:
                    # print("Check:", i, freq[j])
                    add.append(strs[j])
            result.append(add)

        # print(result)

        result2 = []
        for i in result:
            if i not in result2:
                result2.append(i)


        return result2
