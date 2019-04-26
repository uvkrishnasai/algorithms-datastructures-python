def find_second_largest_inorder(root_node):
    arr = []
    helper(root_node, arr)
    assert(len(arr) > 1)
    return arr[-2]


def helper(node, arr):
    if not node:
        return

    helper(node.left, arr)
    arr.append(node.value)
    helper(node.right, arr)


def find_second_largest(root_node):

    assert root_node
    assert(root_node.left or root_node.right)

    node = root_node

    high, sec_high = float("-Inf"), float("-Inf")

    while node:

        val = node.value

        if val > high:
            sec_high, high = high, val
        else:
            if sec_high < val < high:
                sec_high = val

        if node.right:
            node = node.right
        elif node.left:
            node = node.left
        else:
            break

    return sec_high

# Interview cake solution

# If we have a left subtree but not a right subtree,
# then the current node is the largest overall (the "rightmost") node.
# The second largest element must be the largest element in the left subtree.
# We use our find_largest() function above to find the largest in that left subtree!

# If we have a right child, but that right child node doesn't have any children,
# then the right child must be the largest element and our current node must be the second largest element!

# Else, we have a right subtree with more than one element,
# so the largest and second largest are somewhere in that subtree.
# So we step right.


def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)
actual = find_second_largest(tree)
expected = 70
assert(actual == expected)

tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
actual = find_second_largest(tree)
expected = 60
assert(actual == expected)

tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right_left = right.insert_left(60)
right_left_left = right_left.insert_left(55)
right_left.insert_right(65)
right_left_left.insert_right(58)
actual = find_second_largest(tree)
expected = 65
assert(actual == expected)

tree = BinaryTreeNode(50)
left = tree.insert_left(30)
tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
actual = find_second_largest(tree)
expected = 50
assert(actual == expected)

tree = BinaryTreeNode(50)
left = tree.insert_left(40)
left_left = left.insert_left(30)
left_left_left = left_left.insert_left(20)
left_left_left.insert_left(10)
actual = find_second_largest(tree)
expected = 40
assert(actual == expected)

tree = BinaryTreeNode(50)
right = tree.insert_right(60)
right_right = right.insert_right(70)
right_right.insert_right(80)
actual = find_second_largest(tree)
expected = 70
assert(actual == expected)

try:
    tree = BinaryTreeNode(50)
    find_second_largest(tree)
except AssertionError:
    print("AssertionError!")

try:
    find_second_largest(None)
except AssertionError:
    print("AssertionError!")
