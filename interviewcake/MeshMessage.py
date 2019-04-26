from collections import deque


def bfs_get_path(graph, start_node, end_node):

    assert start_node is not None
    assert end_node is not None
    assert graph is not None
    assert start_node in graph

    set_ = set()
    for k, v in graph.items():
        for i in v:
            set_.add(i)

    assert end_node in set_

    if start_node == end_node:
        return [start_node]

    q = deque()
    q.append((start_node, [start_node]))
    visited = set()

    while q:
        node, stack = q.popleft()

        visited.add(node)

        if node in graph:
            for neigh in graph[node]:
                if neigh == end_node:
                    stack.append(neigh)
                    return stack
                if neigh not in visited:
                    q.append((neigh, stack + [neigh]))

    return None


class Test():

    def __init__(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def run_all_tests(self):
        self.test_two_hop_path_1()
        self.test_two_hop_path_2()
        self.test_one_hop_path_1()
        self.test_one_hop_path_2()
        self.test_one_hop_path_3()
        self.test_zero_hop_path()
        self.test_no_path()
        self.test_start_node_not_present()
        self.test_end_node_not_present()

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        assert(actual == expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        assert(actual == expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        assert(actual == expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        assert(actual == expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        assert(actual == expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        assert(actual == expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        assert(actual == expected)

    def test_start_node_not_present(self):
        try:
            bfs_get_path(self.graph, 'h', 'a')
        except AssertionError:
            print("Assertion Error!")

    def test_end_node_not_present(self):
        try:
            bfs_get_path(self.graph, 'a', 'h')
        except AssertionError:
            print("Assertion Error!")


test = Test()
test.run_all_tests()
