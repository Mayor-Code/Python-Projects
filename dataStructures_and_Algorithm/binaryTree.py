class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def tuple_parse(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = tuple_parse(data[0])
        node.right = tuple_parse(data[2])

    elif data is None:
        node = None

    else:
        node = TreeNode(data)
    return node
