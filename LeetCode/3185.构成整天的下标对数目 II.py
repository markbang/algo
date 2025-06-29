#
# @lc app=leetcode.cn id=3185 lang=python3
# @lcpr version=20002
#
# [3185] 构成整天的下标对数目 II
#

from typing import List
# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        H = 24
        ans = 0
        cnt = [0] * H
        for t in hours:
            # 先查询 cnt，再更新 cnt，因为题目要求 i < j
            # 如果先更新，再查询，就把 i = j 的情况也考虑进去了
            ans += cnt[(H - t % H) % H]
            cnt[t % H] += 1
        return ans


# @lc code=end


#
# @lcpr case=start
# [12,12,30,24,24]\n
# @lcpr case=end

# @lcpr case=start
# [72,48,24,3]\n
# @lcpr case=end

#
