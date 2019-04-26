class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_binary_search_tree_using_inorder(root):
    arr = []
    helper(root, arr)
    for i in range(1, len(arr), 1):
        if arr[i] < arr[i-1]:
            return False
    return True


def helper(node, arr):
    if not node:
        return

    helper(node.left, arr)
    arr.append(node.value)
    helper(node.right, arr)


def is_binary_search_tree_using_bfs(root):
    q = [(root, -float("Inf"), float("Inf"))]

    while q:

        node, lower, upper = q.pop()

        #print(node.value, lower, upper)

        if node.value < lower or node.value > upper:
            return False

        if node.left:
            q.append((node.left, lower, node.value))

        if node.right:
            q.append((node.right, node.value, upper))

    return True


def is_binary_search_tree(root):
    return helper_dfs(root, -float("Inf"), float("Inf"))


def helper_dfs(node, lower, upper):
    if not node:
        return True

    if node.value < lower or node.value > upper:
        return False

    return helper_dfs(node.left, lower, node.value) and helper_dfs(node.right, node.value, upper)


tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)
result = is_binary_search_tree(tree)
assert result

tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(80)
left.insert_left(20)
left.insert_right(60)
right.insert_left(70)
right.insert_right(90)
result = is_binary_search_tree(tree)
assert not result

tree = BinaryTreeNode(50)
left = tree.insert_left(40)
left_left = left.insert_left(30)
left_left_left = left_left.insert_left(20)
left_left_left.insert_left(10)
result = is_binary_search_tree(tree)
assert result

tree = BinaryTreeNode(50)
right = tree.insert_right(70)
right_right = right.insert_right(60)
right_right.insert_right(80)
result = is_binary_search_tree(tree)
assert not result

tree = BinaryTreeNode(50)
result = is_binary_search_tree(tree)
assert result
