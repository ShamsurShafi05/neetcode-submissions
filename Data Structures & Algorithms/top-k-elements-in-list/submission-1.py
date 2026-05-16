import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            i = i
            if freq.get(i) == None:
                freq[i] = 1
            else:
                freq[i] += 1

        # print("Frequency:", freq)
        list1 = []
        for key, val in freq.items():
            list1.append([-val, key])

        # print("Before:", list1)

        heapq.heapify(list1)

        # print("After:", list1)

        list2 = []
        for i in range(k):
            list2.append(heapq.heappop(list1)[1])

            # print("Count:", k, "Updated:", list2)
            # print("Remaining:", list1)
        

        # print("\nLast:", list2)
        return list2
