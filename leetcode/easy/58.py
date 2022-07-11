# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s: str) -> int:
    for x in range(len(s)):
        length = len(s.split(" ")[len(s.split(" ")) - 1 - x])
        if length != 0:
            return length


print(lengthOfLastWord("my name is jakub  "))
