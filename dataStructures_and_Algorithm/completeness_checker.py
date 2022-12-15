# For a node to be complete it must have a left node
# for a node to if it has a left node it must have a left node or else it must be the last node on the last level

def isComplete(root):
    stack = [root]
    flag = 0
    while stack:
        node = stack.pop(0)
        if node.left:
            if flag:
                return False
            stack.append(node.left)
        else:
            flag = 1
        if node.right:
            if flag:
                return False
            stack.append(node.right)
        else:
            flag = 1
    return True
