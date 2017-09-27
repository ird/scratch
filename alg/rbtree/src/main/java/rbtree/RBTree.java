package rbtree;

import java.lang.StringBuilder;

class RBTree {
  
  private RBTree left = null;
  private RBTree right = null;
  private RBTree parent;
  private boolean marked = false; //helper when traversing tree 
  private int value;

  private enum Colour { RED, BLACK }
  private Colour colour;

  public RBTree(int value) {
    this.value = value;
    colour = Colour.BLACK;
    parent = null; 
  }

  private RBTree(int value, RBTree parent) {
    this.value = value;
    this.parent = parent;
    this.colour = Colour.RED;
  }

  public void insert(int value, StringBuilder log) { 
    RBTree node =_insert(value, this, log);
    repair(node);
  } 
  
  private static RBTree _insert(int value, RBTree root, StringBuilder log) {
    log.append("_insert("+value+") below "+root.value+"\n");
    if(root.value >= value) {
      if(root.left == null) {
        root.left = new RBTree(value, root);
        return root.left;
      } else {
        _insert(value, root.left, log);
      }
    } else {
      if(root.right == null) {
        root.right = new RBTree(value, root);
        return root.right;
      } else {
        _insert(value, root.right, log);
      }
    }
    return null;
  }

  public static void repair(RBTree node) {

  }

  public String toString() {
    // depth first traversal (l->r)
    StringBuilder sb = new StringBuilder();
    RBTree t = this;
    boolean startState = t.marked; //before toString() is called all nodes' t.marked are the same
    while (t != null) {
      if(t.marked != startState) { 
        t = t.parent;
        continue;
      }
      if((t.left != null) && (t.left.marked == startState)) {
        t = t.left;
        continue;
      }
      sb.append(t.value).append(",");
      t.marked = !startState;
      if(t.right != null) {
        t = t.right;
        continue;
      } 
      t = t.parent;
    }
    return sb.toString();
  }

}
