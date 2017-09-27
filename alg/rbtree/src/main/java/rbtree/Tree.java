package rbtree;

import java.lang.StringBuilder;

class Tree {
    public static Node insert(Node root, int value, StringBuilder log) {
        Node n = new Node(value);
        Node t = root;
        while(t != null) {
            Node p = t;
            if(n.value <= t.value) {
                t = t.left;
                if(t == null) {
                    p.left = n;
                    n.parent = p;
                }
                continue;
            }
            if(n.value > t.value) {
                t = t.right;
                if(t == null) {
                    p.right = n;
                    n.parent = p;
                }
                continue;
            }
        }

        return root;
    }
}
