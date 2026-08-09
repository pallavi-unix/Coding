class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # Root is smallest in binary tree
        min_val = root.val
        
        # Second minimum value node
        self.second_min = float('inf')

        # Using DFS traversal
        def dfs(node):
            if not node:
                return
            
            # If node value is greater than min_val and smaller than current second_min
            if min_val < node.val < self.second_min:
                self.second_min = node.val
            
            # Continue searching left and right subtrees
            dfs(node.left)
            dfs(node.right)

        # Start DFS from the root
        dfs(root)

        # If second_min was never updated then return -1
        return self.second_min if self.second_min != float('inf') else -1


# time Complexity is O(n)
# space complexity is O(h) - height

# Using DFS for below code, I can also use BFS but the space complexity is more as it stores all the nodes at the same level. The task is to find 2nd min value becasue the root is always be the smallest value of the binary tree. The logic is to skip root value and nodes which has same value as root. so with using DFS we find smallest value which is greater than root.
