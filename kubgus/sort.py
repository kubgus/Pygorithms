def sort(nums):
    run = True
    while run:
        curr = -99999999999999  # lowest number that can be in the array
        finished = True
        for index, num in enumerate(nums):
            prev = curr
            curr = num
            if prev > curr:
                finished = False
                nums[index] = prev
                nums[index - 1] = curr
                break
        if finished == True:
            run = False
    return nums


print(sort([9, 8, 420, 9, 7, 5, 8, 3.14, 69, 20, 0, -999, 40, 50, 85.45684]))
