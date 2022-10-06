# Time: O(n)
# Space O(n)

s = "anagram"
t = "nagaram"

def isValidAnagram(s, t):
  if len(s) != len(t):
    return False

  hmap1, hmap2 = {}, {}

  for char in s:
    hmap1[char] = hmap1.get(char, 0) + 1
  for char in t:
    hmap2[char] = hmap2.get(char, 0) + 1
  
  if hmap1 == hmap2:
    return True
  else:
    return False