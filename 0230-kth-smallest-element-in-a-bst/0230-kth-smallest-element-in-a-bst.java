/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private void dfs(TreeNode root, List<Integer> tree) {
        if (root == null) {
            return;
        }
        dfs(root.left, tree);
        tree.add(root.val);
        dfs(root.right, tree);
    }    

    public int kthSmallest(TreeNode root, int k) {
        List<Integer> tree = new ArrayList<>();
        dfs(root, tree);
        return tree.get(k - 1);
    }
}