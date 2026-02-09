class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        self.dfs(root, arr)
        arr.sort()
        return self.construct_BST(arr)
    
    def dfs(self, node, arr):
        if node == None:
            return
        arr.append(node.val)
        self.dfs(node.left, arr)
        self.dfs(node.right, arr)
    
    def construct_BST(self, arr):
        if len(arr) == 0:
            return None
        mid = (len(arr) - 1) // 2
        node = TreeNode(arr[mid])
        node.left = self.construct_BST(arr[:mid])
        node.right = self.construct_BST(arr[(mid+1):])
        return node