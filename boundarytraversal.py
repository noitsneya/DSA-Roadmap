
import java.util.*;

public class Main {
    public static void printBoundary(TreeNode root) {
        if (root == null) return;
        //step 1 - return the root
        System.out.print(root.val + " ");
        //step 2 - left boundary traversal
        printLeftBoundary(root.left);
        //step 3 - leaf nodes
        printLeaf(root.left);
        printLeaf(root.right);
        //step 4 - print right boundary (opposite way, ignoring root)
        printRightBoundary(root.right);
        
    }
    private static void printLeftBoundary(TreeNode node) {
        //left boundary excluding leaf nodes
        while (node != null) {
            if (node.left != null || node.right != null)
                System.out.print(node.val + " ");
            if (node.left != null) {
                node = node.left;
            } else {
                node = node.right;
            }
        }
    }
    
    private static void printLeaf(TreeNode node) {
        //returning leaf nodes here
        if (node == null) return;
            printLeaf(node.left);
        if (node.left == null && node.right == null)
            System.out.print(node.val + " ");
        printLeaf(node.right);
    }
    
    private static void printRightBoundary(TreeNode node) {
        Stack<Integer> stack = new Stack<>();
        while (node != null) {
            if (node.left != null || node.right != null)
                stack.push(node.val);
            if (node.right != null) {
                node = node.right;
            } else {
                node = node.left;
            }
        
    }
    while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }
  }
    
    public static void main(String[] args) {
        // make an arraylist, stack
        TreeNode root = new TreeNode(1); 
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        root.left.right.left = new TreeNode(8);
        root.left.right.right = new TreeNode(9);

        System.out.println("Boundary Traversal:");
        printBoundary(root);
    }
}
// array list is like list in python

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
    
}
