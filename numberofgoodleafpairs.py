""" https://leetcode.com/contest/weekly-contest-199/problems
/number-of-good-leaf-nodes-pairs/
Given the root of a binary tree and an integer distance. 
A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest 
path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length 
of the shortest path between them is 3. This is the only good pair. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pass
        



