# 202. Happy Number
# https://leetcode.com/problems/happy-number/

def isHappy(n: int) -> bool:
    seen = []
    while n != 1:
        prev = n
        if n in seen:
            return False
        seen.append(n)
        for digit in str(prev):
            digit = int(digit)
            n += digit * digit
        n = n - prev
    return True


print(isHappy(19))
