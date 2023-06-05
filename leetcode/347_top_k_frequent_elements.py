"""
Problem Link: https://leetcode.com/problems/top-k-frequent-elements/
"""


class Solution:
    # Time Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = list()
        count_map = dict()
        rev_frequency_table = [[] for i in range((len(nums) + 1))]

        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1

        for key, value in count_map.items():
            rev_frequency_table[value].append(key)

        for i in range(len(rev_frequency_table) - 1, -1, -1):
            for j in rev_frequency_table[i]:
                if k == 0:
                    break
                res.append(j)
                k -= 1
        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: nlogn
        hash_map = dict()
        res = list()
        for i in nums:
            hash_map[str(i)] = hash_map.get(str(i), 0) + 1
        # print(hash_map)
        hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        # print(hash_map)
        
        for key, value in hash_map.items():
            res.append(int(key))
            k -= 1
            if k == 0:
                break
        return res
