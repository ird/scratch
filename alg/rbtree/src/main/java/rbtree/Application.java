package rbtree;

public class Application {

    public static void main(String[] args) {

        StringBuilder log = new StringBuilder();
        RBTree t = new RBTree(8);
        t.insert(3, log);
        t.insert(10, log);
        t.insert(1, log);
        t.insert(6, log);
        t.insert(14, log);
        t.insert(4, log);

        System.out.println(t);
        System.out.print(log.toString());

    //V2

        StringBuilder log2 = new StringBuilder();
        Node t2 = new Node(8);
        Tree.insert(t2, 3, log2);
        Tree.insert(t2, 10, log2);
        Tree.insert(t2, 1, log2);
        Tree.insert(t2, 6, log2);
        Tree.insert(t2, 14, log2);
        Tree.insert(t2, 4, log2);
  }
}
