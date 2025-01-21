# 3110. Score of a String
# https://leetcode.com/problems/score-of-a-string/
class Solution:
    def scoreOfString(self, s: str) -> int:
        tot = 0
        for x in range(len(s) - 1):
            tot = tot + abs(ord(s[x]) - ord(s[x+1]))
        return tot