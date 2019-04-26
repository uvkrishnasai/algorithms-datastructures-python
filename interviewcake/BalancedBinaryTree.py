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


def is_balanced_recursion(root):
    heights = []
    get_height(root, 0, heights)
    max_height = max(heights)
    min_height = min(heights)

    return True if max_height - min_height <= 1 else False


def get_height(node, dept, heights):

    if not node.left and not node.right:
        heights.append(dept)
        return

    if node.left:
        get_height(node.left, dept+1, heights)

    if node.right:
        get_height(node.right, dept+1, heights)


def is_balanced(root):

    if not root:
        return True

    nodes = [(root, 1)]
    min_, max_ = float("Inf"), float("-Inf")

    while nodes:
        node, dept = nodes.pop()

        if not node.left and not node.right:
            min_ = min_ if dept > min_ else dept
            max_ = max_ if dept < max_ else dept
            #print(node.value, min_, max_, dept)

        if node.left:
            nodes.append((node.left, dept+1))

        if node.right:
            nodes.append((node.right, dept+1))

    return True if max_-min_ <= 1 else False


tree = BinaryTreeNode(5)
left = tree.insert_left(8)
right = tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)
result = is_balanced(tree)
print(result)

tree = BinaryTreeNode(3)
left = tree.insert_left(4)
right = tree.insert_right(2)
left.insert_left(1)
right.insert_right(9)
result = is_balanced(tree)
print(result)

tree = BinaryTreeNode(6)
left = tree.insert_left(1)
right = tree.insert_right(0)
right_right = right.insert_right(7)
right_right.insert_right(8)
result = is_balanced(tree)
print(result)

tree = BinaryTreeNode(1)
right = tree.insert_right(2)
right_right = right.insert_right(3)
right_right.insert_right(4)
result = is_balanced(tree)
print(result)
