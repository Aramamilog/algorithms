from collections import deque


# https://leetcode.com/problems/design-hit-counter/description/
# Premium or https://www.lintcode.com/problem/3662/
class HitCounter:

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


hit_counter = HitCounter()
# time complexity O(n)
# memory complexity O(n)

hit_counter.hit(1)
hit_counter.hit(1)
hit_counter.hit(5)
assert hit_counter.getHits(10) == 3
assert hit_counter.getHits(301) == 1
