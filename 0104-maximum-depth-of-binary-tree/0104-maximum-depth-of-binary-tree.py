# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        answer = []

        # 현재 위치 ,현재 층 수
        def dfs(node, depth):
            # 널이 면 리턴
            #왼쪽 or오른쪽으로 내려가기
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
            
            # 왼쪽이랑 오른쪽이 null이면 return
            if node.left is None and node.right is None:
                answer.append(depth)
                return 
        

        dfs(root,1)
        return max(answer)