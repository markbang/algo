#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        dict1 = {"(": ")", "[": "]", "{": "}"}
        keys = dict1.keys()
        for i in s:
            if i in keys:
                list1.append(i)
            elif list1 == []:
                return False
            elif dict1[list1[-1]] == i:
                del list1[-1]
            else:
                return False
        if list1 == []:
            return True
        else:
            return False


# @lc code=end
