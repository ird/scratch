package rbtree;

import java.lang.StringBuilder;

class RBTree {
  
  private RBTree left = null;
  private RBTree right = null;
  private RBTree parent;
  private boolean colour = false; //false is black
  private boolean marked = false; //helper when traversing tree 
  private int value;
  private int bheight = 0;

  public RBTree(int value) {
    this.value = value;
    parent = null; 
  }

  public RBTree(int value, RBTree parent, boolean colour) {
    this.value = value;
    this.parent = parent;
    this.colour = colour;
    if(colour == false) {
      bheight = parent.bheight + 1;
    } else {
      bheight = parent.bheight;
    }
  }

  public void insert(int value, StringBuilder log) { _insert(value, this, log); } 
  
  private void _insert(int value, RBTree root, StringBuilder log) {
    log.append("_insert("+value+") below "+root.value+"\n");
    if(root.value >= value) {
      if(root.left == null) {
        root.left = new RBTree(value, root, !root.colour);
      } else {
        _insert(value, root.left, log);
      }
    } else {
      if(root.right == null) {
        root.right = new RBTree(value, root, !root.colour);
      } else {
        _insert(value, root.right, log);
      }
    }
  }

  public String toString() {
    // depth first traversal (l->r)
    StringBuilder sb = new StringBuilder();
    RBTree t = this;
    boolean startState = t.marked; //before toString() is called all nodes' t.marked are the same
    
    while (t != null) {
      if(t.marked != startState) { 
        // already been traversed
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
