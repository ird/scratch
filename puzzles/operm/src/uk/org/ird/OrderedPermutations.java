package uk.org.ird;

import java.util.Arrays;

public class OrderedPermutations {
    public int[] set;
    public OrderedPermutations(int[] set) {
        this.set = set;
        Arrays.sort(this.set);
    }
    public int[] get(int n) {
        int[] res = set;

        return res;
    }

    @Override
    public String toString() {
        String res = "";
        for(int i=0;i<set.length;++i){
            res += set[i];
        }
        return res;
    }

    public static void main(String[] args) {
        int[] list = {1,0,2};
        OrderedPermutations op = new OrderedPermutations(list);
        System.out.println(op);
    }
}
