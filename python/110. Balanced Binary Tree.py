class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        
        def dfs(node):
            if not node:
                return 0

            L = dfs(node.left)
            R = dfs(node.right)
            if abs(L - R) > 1:
                balanced[0] = False
            
            return 1 + max(L, R) 
        
        dfs(root)
        
        return balanced[0]