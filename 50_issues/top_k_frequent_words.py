from typing import List

import pytest


# https://leetcode.com/problems/top-k-frequent-words/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # time O(n)
        count_map = {}
        for i in words:
            count_map[i] = count_map.get(i, 0) + 1

        # cannot do with * like [[]] * len(words) cause it will be the same objects and append will add to everyone
        freq_bucket = [[] for _ in range(len(words))]

        for word, count in count_map.items():
            freq_bucket[count - 1].append(word)

        result = []
        for freq_nums in freq_bucket[::-1]:
            for word in sorted(freq_nums):
                result.append(word)
                if len(result) == k:
                    return result


sol = Solution()
# time complexity O(n)
# memory complexity O(n)


@pytest.mark.parametrize(
    "words, k, expected",
    [
        (["i","love","leetcode","i","love","coding"], 2, ["i","love"]),
    ]
)
def test_topKFrequent(words, k, expected):
    assert sol.topKFrequent(words, k) == expected
