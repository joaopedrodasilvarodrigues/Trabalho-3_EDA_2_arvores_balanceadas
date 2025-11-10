class RedBlackTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
        self.isRed = True


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def sizeOf(self, node):
        return node.size if node else 0

    @property
    def size(self):
        return self.sizeOf(self.root)

    def rotateLeft(self, root):
        right = root.right

        root.size, right.size = self.sizeOf(
            root.left) + self.sizeOf(right.left) + 1, root.size

        root.right = right.left
        right.left = root

        right.isRed = root.isRed
        root.isRed = True

        return right

    def rotateRight(self, root):
        left = root.left

        root.size, left.size = self.sizeOf(
            root.right) + self.sizeOf(left.right) + 1, root.size

        root.left = left.right
        left.right = root

        left.isRed = root.isRed
        root.isRed = True

        return left

    def flipColor(self, root):
        root.left.isRed = False
        root.right.isRed = False
        root.isRed = True
        return root

    def insertTo(self, root, val):
        if not root:
            return RedBlackTreeNode(val)

        if val > root.val:
            root.right = self.insertTo(root.right, val)
        else:
            root.left = self.insertTo(root.left, val)

        if (root.right and root.right.isRed) and not (
                root.left and root.left.isRed):
            root = self.rotateLeft(root)

        if (root.left and root.left.isRed) and (
                root.left.left and root.left.left.isRed):
            root = self.rotateRight(root)

        if (root.left and root.left.isRed) and (
                root.right and root.right.isRed):
            root = self.flipColor(root)

        root.size = sum(map(self.sizeOf, (root.left, root.right))) + 1
        return root

    def insert(self, val):
        self.root = self.insertTo(self.root, val)
        self.root.isRed = False

    def searchK(self, k, root=None):
        root = root or self.root

        size = self.sizeOf(root.left) + 1
        if k == size:
            return root.val

        return self.searchK(k, root.left) if k < size else self.searchK(
            k - size, root.right)


class MedianFinder(object):
    def __init__(self):
        self.tree = RedBlackTree()

    def addNum(self, num):
        self.tree.insert(num)

    def findMedian(self):
        size = self.tree.size
        if size & 1:
            return self.tree.searchK(size + 1 >> 1)
        return sum(map(self.tree.searchK, (size >> 1, size + 2 >> 1))) / 2.0