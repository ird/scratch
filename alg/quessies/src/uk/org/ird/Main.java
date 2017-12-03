package uk.org.ird;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Main {

    private static void qsort(LinkedList<Integer> A, int low, int high) {
        if (low < high) {
            int p = pivot(A, low, high);
            qsort(A, low, p);
            qsort(A, p+1, high);
        }

    }

    private static int pivot(LinkedList<Integer> A, int low, int high) {
        int pivotValue = A.get(high-1);
        int pivotPos = A.indexOf(pivotValue);
        for (int i=low; i<=high; ++i) {
            if (A.get(i) > pivotValue && i < pivotPos) {
                int e = A.remove(i);
                A.add(pivotPos, e);
                pivotPos--;
            }
            if (A.get(i) < pivotValue && i > pivotPos) {
                int e = A.remove(i);
                A.add(pivotPos-1, e);
                pivotPos++;
            }
        }
        return A.indexOf(pivotValue);
    }

    private static LinkedList<Integer> bubblesort(LinkedList<Integer> unsorted) {
        LinkedList<Integer> list = new LinkedList<>(unsorted);
        for (int i=0; i<list.size(); ++i) {
            for (int j=i; j<list.size(); ++j){
                if(list.get(i) > list.get(j)) {
                    int n = list.get(j);
                    list.set(j, list.get(i));
                    list.set(i, n);
                }
            }
        }
        return list;
    }

    private static LinkedList<Integer> insertionsort(LinkedList<Integer> unsorted) {
        LinkedList<Integer> res = new LinkedList<>();
        for (int e : unsorted) {
            int i=0;
            for(; i<res.size(); ++i) {
                if(e < res.get(i)) {
                    break;
                }
            }
            res.add(i, e);
        }
        return res;
    }

    public static void main(String[] args) {
        final String template = "Item: %x, Posn: %x";
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8);
        for (int e: list) {
            //System.out.println(String.format(template, e, list.indexOf(e)));
        }

        LinkedList<Integer> u = new LinkedList<Integer>(Arrays.asList(5,20,1,10,100,32,11));
        // System.out.println(bubblesort(u));
        // System.out.println(insertionsort(u));
        System.out.println("Before qsort: "+ u);
        qsort(u, 0, u.size()-1);
        System.out.println("After qsort: " + u);
    }
}
