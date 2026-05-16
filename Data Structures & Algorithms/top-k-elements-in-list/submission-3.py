import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in range(len(nums)+1):
            freq.append([])

        freqd = {}
        for i in nums:
            # if freqd.get(i) == None:
            #     freqd[i] = 1
            # else:
            #     freqd[i] += 1
            freqd[i] = 1 + freqd.get(i, 0)

        for key, val in freqd.items():
            freq[val].append(key)

        count = 0
        result = []
        for i in range(len(freq)-1, -1, -1):
            if len(freq[i]) != 0:
                result.extend(freq[i])
                count += len(freq[i])
                if count == k:
                    break
                

        return result
