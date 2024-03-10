def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.data)
    Inorder(root.right)


# Iterative inorder traversal using stack
def InorderIterative(root):
    if root is None:
        return
    stack = [root]
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.data)
        root = root.right
