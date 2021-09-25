#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=len(nums)
        for i in range(-L,-1):
            if nums[i]>target:
                del nums[i]
        return nums

# @lc code=end