# recursive Postorder traversal
def Postorder(root):
    if root is None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.data)


# Iterative Postorder traversal
'''
Post order needs to be processed differently than preorder or inorder, because this needs us to process left and 
right before the root node
-> we can use 2 stacks 
'''


def postorder(root):
    if not root:
        return

    stack = [root]
    # the res array is stored in reverse order (root, right, left) so we need to reverse it at the end
    res = []
    while stack:
        node = stack.pop()
        res.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res[::-1]
