from typing import List

class Node:
    NIL = None  # será definido após a classe

    def __init__(self, value=None):
        self.value = value
        self.value_count = 0
        self.total_count = 0
        self.color = 'BLACK'
        self.parent = None
        self.left = None
        self.right = None

# Inicializa o nó NIL (sentinela)
Node.NIL = Node()
Node.NIL.left = Node.NIL.right = Node.NIL.parent = Node.NIL


class RedBlackTree:
    def __init__(self):
        self.root = Node.NIL

    def add(self, value):
        current = self.root
        prev = Node.NIL

        while current != Node.NIL and current.value != value:
            current.total_count += 1
            prev = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current != Node.NIL:
            current.total_count += 1
            current.value_count += 1
            return

        node = Node(value)
        node.value_count = node.total_count = 1
        node.color = 'RED'
        node.left = node.right = node.parent = Node.NIL

        if prev == Node.NIL:
            self.root = node
        else:
            node.parent = prev
            if value < prev.value:
                prev.left = node
            else:
                prev.right = node

        # Balanceamento rubro-negro
        self._balance_after_insert(node)
        self.root.color = 'BLACK'

    def _balance_after_insert(self, node):
        while node.parent.color == 'RED':
            parent = node.parent
            granddad = parent.parent
            left = (granddad.left == parent)
            uncle = granddad.right if left else granddad.left

            if uncle.color == 'RED':
                granddad.color = 'RED'
                parent.color = uncle.color = 'BLACK'
                node = granddad
            else:
                if (left and parent.right == node) or (not left and parent.left == node):
                    node = parent
                    self._rotate(node, left)
                parent.color = 'BLACK'
                granddad.color = 'RED'
                self._rotate(granddad, not left)

    def _rotate(self, node, left):
        parent = node.parent
        child = node.right if left else node.left

        if left:
            node.right = child.left
            if child.left != Node.NIL:
                child.left.parent = node
        else:
            node.left = child.right
            if child.right != Node.NIL:
                child.right.parent = node

        node.total_count = node.left.total_count + node.value_count + node.right.total_count
        child.parent = parent

        if parent == Node.NIL:
            self.root = child
        else:
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child

        if left:
            child.left = node
        else:
            child.right = node

        node.parent = child
        child.total_count = child.left.total_count + child.value_count + child.right.total_count
        Node.NIL.left = Node.NIL.right = Node.NIL.parent = Node.NIL


def countLE(root, value):
    current = root
    count = current.total_count
    while current != Node.NIL:
        if current.value == value:
            count -= current.right.total_count
            break
        elif value < current.value:
            count -= current.value_count + current.right.total_count
            current = current.left
        else:
            current = current.right
    return count


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sum_val = 0
        tree = RedBlackTree()
        tree.add(sum_val)  # prefixo vazio
        count = 0

        for num in nums:
            sum_val += num
            count += countLE(tree.root, sum_val - lower) - countLE(tree.root, sum_val - upper - 1)
            tree.add(sum_val)

        return count
