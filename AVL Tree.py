class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    update_height(y)
    update_height(x)
    return x

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    update_height(x)
    update_height(y)
    return y

def balance_factor(node):
    return height(node.left) - height(node.right)


def deleteNode(root, key):
    # code here
    # return root of edited tree
  
    if not root:
        return None
    
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        succ = root.right
        while succ.left:
            succ = succ.left
        root.data = succ.data
        root.right = deleteNode(root.right, succ.data)
    
    update_height(root)
    
    balance = balance_factor(root)
    
    if balance > 1:
        if balance_factor(root.left) >= 0:
            return right_rotate(root)
        root.left = left_rotate(root.left)
        return right_rotate(root)
    
    if balance < -1:
        if balance_factor(root.right) <= 0:
            return left_rotate(root)
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

 
