class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:

    def __init__(self):
        self.root = None

    def add(self, value):
        self.root = self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value <= current_node.value:
            current_node.left_child = self._add_recursive(current_node.left_child, value)
        else:
            current_node.right_child = self._add_recursive(current_node.right_child, value)

    def _contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)

    def contains(self, value):
        return self._contains(self.root, value)
