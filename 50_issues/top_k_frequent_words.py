from typing import List

import heapq
import pytest


# https://leetcode.com/problems/top-k-frequent-words/



class HeapItem:
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq

        # Lexicographically larger words have lower priority.
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_map = {}
        for i in words:
            count_map[i] = count_map.get(i, 0) + 1

        # FIRST DECISION
        # cannot do with * like [[]] * len(words) cause it will be the same objects and append will add to everyone
        # freq_bucket = [[] for _ in range(len(words))]
        #
        # for word, count in count_map.items():
        #     freq_bucket[count - 1].append(word)
        #
        # result = []
        # for i in range(len(freq_bucket) - 1, -1, -1):
        #     for word in sorted(freq_bucket[i]):
        #         result.append(word)
        #         if len(result) == k:
        #             return result

        # SECOND DECISION
        heap = []

        for word, freq in count_map.items():
            heapq.heappush(heap, HeapItem(word, freq))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap).word)

        return result[::-1]


sol = Solution()
# FIRST DECISION
# time complexity O(n*logn)
# memory complexity O(n)

# SECOND DECISION
# time complexity O(n*logk) for k ≥ 2
# memory complexity O(m+k)


@pytest.mark.parametrize(
    "words, k, expected",
    [
        (["i","love","leetcode","i","love","coding"], 2, ["i","love"]),
    ]
)
def test_topKFrequent(words, k, expected):
    assert sol.topKFrequent(words, k) == expected


@pytest.mark.parametrize(
    "words, k, expected",
    [
        (
            ["i", "love", "leetcode", "i", "love", "coding"],
            2,
            ["i", "love"],
        ),
        (
            ["the", "day", "is", "sunny", "the", "the",
             "the", "sunny", "is", "is"],
            4,
            ["the", "is", "sunny", "day"],
        ),
        (
            ["dog", "cat", "apple", "banana"],
            1,
            ["apple"],
        ),
        (
            ["zebra", "apple", "banana", "zebra", "apple", "banana"],
            2,
            ["apple", "banana"],
        ),
        (
            ["hello"],
            1,
            ["hello"],
        ),
    ],
)
def test_topKFrequent(words, k, expected):
    assert Solution().topKFrequent(words, k) == expected
