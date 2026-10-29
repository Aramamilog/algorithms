from typing import List

import pytest


# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1

        freq_bucket = [[] for _ in range(len(nums))]  # can not do with * like [[]] * len(nums) cause it will be the same objects and append will add to everyone

        for num, count in count_map.items():
            freq_bucket[count - 1].append(num)

        result = []
        for freq_nums in freq_bucket[::-1]:
            for num in freq_nums:
                result.append(num)
                if len(result) == k:
                    return result



sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1,1,1,2,2,3], 2, [1,2]),
    ]
)
def test_topKFrequent(nums, k, expected):
    assert sol.topKFrequent(nums, k) == expected
