# 1. Two Sum
# https://leetcode.com/problems/two-sum/

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, num in enumerate(nums):
        if target - num in seen:
            return [index, seen[target - num]]
        seen[num] = index


print(twoSum([4, -2, 5, 0, 6, 3, 2, 7], 1))
