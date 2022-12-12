class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def traverse_in_order(node):
        if node is None:
            return []
        checked = [node]
        result = []
        left_check = False
        while len(checked) > 0:
            pointer = checked[len(checked) - 1]
            if (not pointer.left is None) and not left_check:
                left_check = False
                checked.append(pointer.left)
                continue
            result.append(pointer.key)
            left_check = True
            checked.pop()
            if not pointer.right is None:
                checked.append(pointer.right)
                left_check = False
        return result
