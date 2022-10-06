# Time: O(n)
# Space: O(n)

s1 = '{([])}'
s2 = '(]'
s3 = '{'

def isValidParentheses(s):

  stack = []
  closeToOpen = {')': '(', ']': '[', '}': '{'}

  for char in s:
    if char in closeToOpen:
      if stack and stack[-1] == closeToOpen[char]:
        stack.pop()
      else:
        return False
    else:
      stack.append(char)
  
  return stack == []
