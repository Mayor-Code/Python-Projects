from dataStructures_and_Algorithm.binaryTree import tuple_parse


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    # function to get the distance of leaf node from the root and get some incomplete node
    @staticmethod
    def leafNodeDistance(tree):
        if tree is None:
            return 0

        def traverse(node, distance=0):
            if node is None:
                return []

            result = traverse(node.left, distance + 1)

            # if the binary is not fill from left to right
            if node.left is None and not (node.right is None):
                result.append((None, 0))

            # if there is an incomplete node
            if not (node.left is None) and node.right is None:
                result.append((None, -1))

            # put the leaf node and it distance in list
            if node.left is None and node.right is None:
                result.append((node.key, distance))
                return result

            result += traverse(node.right, distance + 1)

            return result

        return traverse(tree)

    def isCompleteTree(self):
        not_full = 0
        leaf_nodes = TreeNode.leafNodeDistance(self)
        print(leaf_nodes)

        # make sure the height of the list is equal to the first leaf node from the left
        legal_height = leaf_nodes[0][1]

        # if there is only one node
        if len(leaf_nodes) == 1:
            return True

        for leaf in leaf_nodes:

            # catch incomplete node
            if leaf[1] == -1 or legal_height != leaf[1]:
                not_full += 1
                legal_height -= 1

            # catch is not fill from left to right or more than one incomplete node
            if leaf[1] == 0 or legal_height < leaf[1] or not_full >= 2:
                return False
        return True


tuple1 = ((((15, 8, None), 4, 9), 2, (10, 5, 11)), 1, ((12, 6, 13), 3, (None, 7, None)))
tuple2 = (2, 1, None)
tuple3 = ((5, 2, None), 1, (7, 3, 8))
tree1 = tuple_parse(tuple1)
tree2 = tuple_parse(tuple2)
tree3 = tuple_parse(tuple3)
print(tree1)

print(TreeNode.isCompleteTree(tree1))
print(TreeNode.isCompleteTree(tree2))
print(TreeNode.isCompleteTree(tree3))
