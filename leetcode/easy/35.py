# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums: list[int], target: int):
    if target > nums[len(nums) - 1]:
        return len(nums)
    if target < nums[0]:
        return 0
    for index, num in enumerate(nums):
        if num == target:
            return index
    for index, num in enumerate(nums):
        if index - 1 >= 0 and nums[index - 1] < target and nums[index] > target:
            return index


print(searchInsert([1, 2, 5, 7, 12, 69], 3))
