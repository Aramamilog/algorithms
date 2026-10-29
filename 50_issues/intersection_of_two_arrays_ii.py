import pytest


# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # FIRST decision

        map_1, map_2 = {}, {}

        for i in nums1:
            map_1[i] = 1 + map_1.get(i, 0)

        for i in nums2:
            map_2[i] = 1 + map_2.get(i, 0)

        res = []
        for k in map_1:
            map_1_size = map_1[k]
            map_2_size = map_2.get(k, 0)

            if not map_2_size:
                continue

            to_extend = [k] * min(map_1_size, map_2_size)
            res.extend(to_extend)

        # Time:  O(n + m)
        # Space: O(u1 + u2 + k), где u1/u2 — количество уникальных элементов + пересечение
        return res

        # SECOND decision

        # first follow up:  if arrays are sorted - this algo with two pointers are optimized
        #   than previouse one

        # second follow up: nums1's size small compared to nums2's size - this algo better
        #   cause we will exit from the while loop after nums1 array will exhausted

        # assume that input already sorted
        nums1.sort()
        nums2.sort()

        l, r = 0, 0
        res = []

        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                res.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1

        return res

        # THIRD FOLLOW-UP
        #
        # What if nums2 is stored on disk and the memory is limited,
        # so we cannot load the entire array into memory?
        #
        # If nums1 is small enough to fit into memory, we can build
        # a frequency map for nums1 and process nums2 in chunks.
        #
        # We never load the entire nums2 into memory.
        # Instead, we read a small chunk, process it, and then move
        # to the next chunk.
        #
        # Example:
        #
        # nums1 = [1, 2, 2, 3]
        #
        # nums2 is stored on disk:
        # [10, 2, 7, 2, 8] -> [3, 100, 5] -> ...
        #
        # We keep only nums1's frequency map in memory:
        # {
        #     1: 1,
        #     2: 2,
        #     3: 1
        # }
        #
        # Then we process nums2 chunk by chunk.

        from collections import Counter

        def intersect_from_disk(nums1, nums2_file):
            counter = Counter(nums1)
            result = []

            # Read nums2 incrementally instead of loading the entire file.
            for chunk in nums2_file:
                for num in chunk:
                    if counter[num] > 0:
                        result.append(num)
                        counter[num] -= 1

            return result


sol = Solution()


# FIRST decision
# time complexity O(n + m)
# memory complexity O(k) - intersections

# SECOND decision
# time complexity O(n)
# memory complexity O(n) + O(nlogn) = O(n)

# THIRD FOLLOW-UP
# time complexity O(len(nums1) + len(nums2))
# memory complexity O(unique(nums1) + chunk_size)


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1,2,2,1], [2,2], [2,2]),
    ]
)
def test_intersect(nums1, nums2, expected):
    assert sol.intersect(nums1, nums2) == expected
