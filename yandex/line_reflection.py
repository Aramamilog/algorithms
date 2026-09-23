from typing import List


# https://leetcode.com/problems/line-reflection/description/
# Only with subscription
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # Problem:
        # Задача 32: Симметрия относительно линии [Medium]
        # Источник: LeetCode 356
        #
        # Тема: Геометрия, HashSet
        #
        # Подходит для практики: Занятие 2 (HashMap и HashSet)
        #
        # Последний раз видели: до 2026
        #
        # Дано n точек на двумерной плоскости. Необходимо определить, существует ли линия, параллельная оси y, которая отражает заданные точки.
        #
        # Более формально: нужно найти, существует ли линия x = k такая, что для каждой точки (x, y) существует соответствующая точка (2k - x, y).
        #
        # Пример:
        #
        # Вход: points = [[1,1],[-1,1]]
        # Выход: true
        #
        # Вход: points = [[1,1],[-1,-1]]
        # Выход: false
        #
        # Требования:
        # Временная сложность: O(n)
        # Пространственная сложность: O(n)
        # points length >= 1

        points_set = {(x, y) for x, y in points}

        max_x = max(x for x, _ in points_set)
        min_x = min(x for x, _ in points_set)

        reflection_sum = min_x + max_x

        for x, y in points_set:
            reflected = (reflection_sum - x, y)
            if reflected not in points_set:
                return False

        return True


sol = Solution()
assert sol.isReflected([[1,1],[-1,1]]) == True
assert sol.isReflected([[1,1],[-1,-1]]) == False
# time complexity O(n)
# memory complexity O(n)
