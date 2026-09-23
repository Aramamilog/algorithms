from typing import List


# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # first decision
        # if s and t consist of lowercase English letters

        # count_s = [0] * 26
        # count_t = [0] * 26
        # for s_char, t_char in zip(s, t):
        #     s_index = ord(s_char) - ord('a')
        #     t_index = ord(t_char) - ord('a')

        #     count_s[s_index] +=1
        #     count_t[t_index] +=1

        # return count_s == count_t

        # second decision
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        for i in count_s:
            if count_s[i] != count_t.get(i, 0):
                return False

        return True


sol = Solution()
assert sol.isAnagram("anagram", "nagaram") == True
assert sol.isAnagram("rat", "car") == False
# first decision
# time complexity O(len(s/t))
# memory complexity O(52)

# second decision
# time complexity O(len(s/t))
# memory complexity O(s) + O(t) = O(c)
