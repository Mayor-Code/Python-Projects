class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None
    root = TreeNode(preorder[0])
    if len(preorder) == 1:
        return root
    mid = None
    for i in range(len(inorder)):
        if preorder[0] == inorder[i]:
            mid = i
            break
    left_inorder, right_inorder = inorder[:mid], inorder[mid + 1:]
    left_preorder, right_preorder = preorder[1:mid + 1], preorder[mid + 1:]
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)
    return root

