# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # ganho máximo do lado esquerdo/direito (se negativo, ignoramos com max(0, ...))
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # caminho passando pelo nó atual como "topo"
            current_path = node.val + left_gain + right_gain

            # atualiza o máximo global
            self.max_sum = max(self.max_sum, current_path)

            # retorna o ganho máximo se continuar o caminho para cima
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
