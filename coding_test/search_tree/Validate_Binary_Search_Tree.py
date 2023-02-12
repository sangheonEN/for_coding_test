from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        inf = 1e8
        root = TreeNode(root[0], root[1], root[2])

        def solve(node, left, right) -> bool:
            if not node:
                return True

            if node.val <= left or node.val >= right:
                return False

            ret = solve(node.left, left, node.val) and solve(node.right, node.val, right)

            return ret

        return solve(root, -inf, inf)


if __name__ == "__main__":
    root = [2,1,3]
    VBST = Solution()
    result = VBST.isValidBST(root)
    print(result)