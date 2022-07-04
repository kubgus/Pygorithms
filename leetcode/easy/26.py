# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums) -> int:
    curr = -101
    index = 0
    for num in nums:
        prev = curr
        curr = num
        if curr != prev:
            nums[index] = curr
            index += 1
    return index


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
