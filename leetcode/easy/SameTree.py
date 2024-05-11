# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 전혀 모르겠어서 풀이 찾아봤다^^
# 깊이 우선 탐색은 제발 재귀함수를 쓸 생각을 하자
# p와 q 모두 null일 경우 같은 트리
# p와 q 둘 중 하나만 null이거나 값이 같지 않다면 다른 트리
# p와 q의 값이 같다면 그 다음 노드 탐색 -> 재귀함수, 양쪽으로 노드가 있으므로 left 노드 right 노드 따로 탐색
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        if p.val==q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
