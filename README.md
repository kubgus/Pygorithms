<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png" alt="Python Logo" width="500"/>  
  
# Pygorithms
A little repository I'm going to be working on for the next couple of weeks. (probably)  
It's basically a collection of algorithms in Python.  
  
## It's my code
The algorithms are done by me, so they aren't going to be super efficient.  
Feel free to use them, though...  
## Goals
I hope these aren't going to end up forgotten like my C++ repository...  
- [x] 1 algorithm  
- [ ] 10 algorithms  
- [ ] 20 algorithms  
- [ ] 30 algorithms  

## Example
```py
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
```
