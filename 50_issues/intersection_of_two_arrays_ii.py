import pytest

from collections import Counter


# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Hash map approach."""
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)

        result = []

        for num, count in counts1.items():
            result.extend([num] * min(count, counts2.get(num, 0)))

        return result

    def intersect_sorted(
        self, nums1: list[int], nums2: list[int]
    ) -> list[int]:
        """Two pointers. Both input arrays must already be sorted."""
        left, right = 0, 0
        result = []

        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                result.append(nums1[left])
                left += 1
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1

        return result

    def intersect_from_disk(self, nums1, nums2_chunks):
        """Process nums2 incrementally without loading it into memory."""
        counts = Counter(nums1)
        result = []

        for chunk in nums2_chunks:
            for num in chunk:
                if counts[num] > 0:
                    result.append(num)
                    counts[num] -= 1

        return result

    def intersect_small_first(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result


sol = Solution()


# Hash map approach:
# Time: O(n + m)
# Space: O(u1 + u2 + k)

# Two pointers (already sorted inputs):
# Time: O(n + m)
# Auxiliary space: O(1)
# Output space: O(k)

# Two pointers (sorting required):
# Time: O(n log n + m log m)
# Auxiliary space: O(n + m) worst case with Python's sort

# Hash map for the smaller array:
# Time: O(n + m)
# Space: O(min(n, m) + k)

# Disk-based processing:
# Time: O(n + m)
# Space: O(u1 + chunk_size + k)


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 2, 3], [4, 5, 6], []),
        ([1, 1, 1], [1, 1], [1, 1]),
        ([], [1, 2], []),
    ],
)
def test_intersect(nums1, nums2, expected):
    assert sorted(sol.intersect(nums1, nums2)) == sorted(expected)

    assert sorted(sol.intersect_sorted(sorted(nums1), sorted(nums2))) == sorted(expected)

    assert sorted(sol.intersect_small_first(nums1, nums2)) == sorted(expected)

    # Simulate disk chunks.
    chunks = [nums2[i:i + 2] for i in range(0, len(nums2), 2)]

    assert sorted(sol.intersect_from_disk(nums1, chunks)) == sorted(expected)
