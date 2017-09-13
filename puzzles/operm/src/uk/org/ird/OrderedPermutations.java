package uk.org.ird;

import java.util.Arrays;

public class OrderedPermutations {
    private int[] set;
    public OrderedPermutations(int[] set) {
        this.set = set;
        Arrays.sort(this.set);
    }
    public void succ(int n) {
        int i=0;
        while(i != n){
            int k = lastOrderedPairIndex();
            if(k == -1){
                //reached last permutation
                break;
            }
            int j = set.length -1;
            for(; j > k; j--){
                if(set[j] > set[k])
                    break;
            }
            swap(k,j);
            reverseToEnd(k+1);
            i++;
        }
    }
    private int lastOrderedPairIndex(){
        for(int i=set.length-2; i>=0; i--){
            if(set[i] < set[i+1])
                return i;
        }
        return -1; //done
    }
    private void swap(int i, int j) {
        int t = set[i];
        set[i] = set[j];
        set[j] = t;
    }
    private void reverseToEnd(int i) { //inclusive of i
        int[] subSet = Arrays.copyOfRange(set,i,set.length);
        int j = subSet.length-1;
        for(int k=i;k<set.length;++k){
            set[k] = subSet[j];
            j--;
        }
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
        int[] list = {0,1,2,3,4,5,6,7,8,9};
        OrderedPermutations op = new OrderedPermutations(list);
        op.succ(1000000);
        System.out.println(op);
    }
}
