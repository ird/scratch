package uk.org.ird;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.stream.Collectors;

public class OrderedPermutations2 {
    public LinkedList<Integer> list;
    public OrderedPermutations2(final LinkedList<Integer> list) {
        this.list = list.stream().sorted().collect(Collectors.toCollection(LinkedList::new));
    }
    public void succ(final int n) {
        //
        for(int i=0; i<n; i++){
            int k = list.size();
            Iterator it = list.descendingIterator();
            while(it.hasNext()){

            }
        }
    }
    @Override
    public String toString() {
        return list.toString();
    }
}
