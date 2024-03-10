# recursive preorder traversal
def Preorder(root):
    if root is None:
        return
    print(root.data)
    Preorder(root.left)
    Preorder(root.right)


# iterative preorder traversal
def PreorderIter(root):
    curr = root
    stack = []
    while stack or curr:
        while curr:
            stack.append(curr)
            print(curr.data)
            curr = curr.left

        poppedNode = stack.pop()
        curr = poppedNode.right
