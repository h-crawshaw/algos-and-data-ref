def invertTree(root):

  tmp = root.left
  root.left = root.right
  root.right = tmp

  self.invertTree(root.left)
  self.invertTree(root.right)
  return root