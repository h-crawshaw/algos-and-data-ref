s = "abcabcbb"

l, r = 0, 2
subslen = 0

def maxsubslen(s):
  l, r = 0, 1
  substring_length = 0
  
  while r < len(s):
    subs = s[l]
    while r < len(s) and s[r] not in subs:
      subs += s[r]
      r += 1
      current_subslength = r - l
      substring_length = max(substring_length, current_subslength)
    if subs[r] in subs:
      l = r
  return substring_length

print(maxsubslen(s))

  


