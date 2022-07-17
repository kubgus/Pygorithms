# 66. Plus One
# https://leetcode.com/problems/plus-one/

def plusOne(digits: list[int]) -> list[int]:
    digits[len(digits)-1] += 1
    for index, digit in enumerate(reversed(digits)):
        if digit >= 10:
            digits[len(digits) - 1 - index] = 0
            if len(digits) - 2 - index < 0:
                digits[len(digits) - 1 - index] += 1
                digits.append(0)
            else:
                digits[len(digits) - 2 - index] += 1
        else:
            return digits
    return digits

    # return [int(x) for x in str(int("".join(map(str, digits))) + 1)]
    # ^ alternative solution one-liner (cheating)


print(plusOne([6, 8]))
