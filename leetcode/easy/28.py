# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/

def strStr(haystack: str, needle: str):
    for index, letter in enumerate(haystack):
        if letter == needle[0]:
            for i in range(len(needle)):
                if len(haystack) <= index + i or haystack[index+i] != needle[i]:
                    break
            else:
                return index
    return -1


print(strStr("mississippi", "issip"))
