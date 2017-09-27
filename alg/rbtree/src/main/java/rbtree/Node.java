package rbtree;

class Node {
    public Node left, right, parent;
    public Colour colour;
    public final int value;

    public Node(int value) {
        this.value = value;
        left = null;
        right = null;
        colour = Colour.RED;
    }
}


