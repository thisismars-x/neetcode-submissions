# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        def _preorder(
            rnode: TreeNode | None,
            snode: TreeNode | None,
            compare: bool = False
        ) -> bool:

            if not snode:
                return not rnode if compare else True

            if not rnode:
                return False

            if rnode.val == snode.val:
                if (
                    _preorder(rnode.left, snode.left, True)
                    and _preorder(rnode.right, snode.right, True)
                ):
                    return True

            if compare:
                return False

            return (
                _preorder(rnode.left, subRoot)
                or _preorder(rnode.right, subRoot)
            )

        return _preorder(root, subRoot)