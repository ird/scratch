package uk.org.ird;

import java.util.Collections;
import java.util.LinkedList;
import java.util.stream.Collectors;

public class OrderedPermutations2 {
    public LinkedList<Integer> list;
    public OrderedPermutations2(final LinkedList<Integer> list) {
        this.list = list.stream().sorted().collect(Collectors.toCollection(LinkedList::new));
    }
    public void succ(int n) {
        for (; n > 0; n--) {
            int k;
            if ((k = lastOrderedPairIndex()) == -1) {
                break; // already on the last ordered permutation
            } else {
                Collections.swap(list, k, rightmostGt(k));
                Collections.reverse(list.subList(k+1, list.size()));
            }
        }
    }

    @Override
    public String toString() {
        return list.toString();
    }

    private int lastOrderedPairIndex() {
        for(int i=list.size() - 2; i>=0; i--){
            if(list.get(i) < list.get(i+1))
                return i;
        }
        return -1; //done
    }

    private int rightmostGt(int k) {
        for(int j = list.size() - 1; j > k; j--) {
            if (list.get(k) < list.get(j))
                return j;
        }
        return k+1; //by definition - won't get here
    }
}
