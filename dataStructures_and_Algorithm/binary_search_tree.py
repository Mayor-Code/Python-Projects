def remove_None(nums):
    return [x for x in nums if x is not None]


def insert(node, key, value=None):
    if node is None:
        return BSTNode(key, value)
    if key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    if key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

def make_balanced_bst(data, lo=0, hi=None):
    if not hi:
        hi = len(data)-1
    while lo < hi:
        mid = (lo+hi)//2
        key, value = data[mid]
        root = BSTNode(key, value)
        root.left = make_balanced_bst(data, 0, mid-1)
        root.right = make_balanced_bst(data, mid+1)

    return root


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_bst(self, tree):
        if tree is None:
            return True, None, None
        is_bst_l, min_l, max_l = self.is_bst(tree.left)
        is_bst_r, min_r, max_r = self.is_bst(tree.right)

        is_bst_node = ((is_bst_l and is_bst_l) and
                       (min_l is None or min_l < tree.key) and
                       (min_r is None or min_r > tree.key))

        min_key = min(remove_None([min_r, tree.key, min_r]))
        max_key = min(remove_None([max_l, tree.key, max_r]))
        return is_bst_node, min_key, max_key

    def size(self):
        if self is None:
            return 0
        return 1 + BSTNode.size(self.left) + BSTNode.size(self.right)

    def height(self):
        if self is None:
            return 0
        return 1 + max(BSTNode.height(self.left), BSTNode.height(self.right))

    def display_tree(self, space="\t", level=0):
        if self is None:
            print(space * level + "∅")
            return ""

        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return ""

        print(BSTNode.display_tree(self.right, space, level + 1))
        print(space * level + str(self.key))
        print(BSTNode.display_tree(self.left, space, level + 1))
        return ""

    def is_balance(self):
        if self is None:
            return True

        is_bal_l = BSTNode.is_balance(self.left)
        is_bal_r = BSTNode.is_balance(self.right)

        return is_bal_r and is_bal_l and abs(BSTNode.height(self.right) - BSTNode.height(self.left)) <= 1

    def listAll(self):
        if self is None:
            return []
        return BSTNode.listAll(self.left) + [(self.key, self.value)] + BSTNode.listAll(self.right)
