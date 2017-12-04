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
        int pivot = high - 1;
        for (int i=low; i<=high; i++) {
            if (A.get(i) > A.get(pivot) && i < pivot) {
                int e = A.remove(i);
                A.add(pivot, e);
                pivot--;
            }
            if (A.get(i) < A.get(pivot) && i > pivot) {
                int e = A.remove(i);
                A.add(pivot-1, e);
                pivot++;
            }
        }
        return pivot;
    }

    private static LinkedList<Integer> mergesort(LinkedList<Integer> unsorted) {
        if(unsorted.size() == 1) {
            return unsorted;
        }
        LinkedList<Integer> left = new LinkedList<>();
        LinkedList<Integer> right = new LinkedList<>();
        int i = 0;
        for (; i < unsorted.size()/2; i++) {
            left.add(unsorted.get(i));
        }
        for(; i< unsorted.size(); i++) {
            right.add(unsorted.get(i));
        }
        left = mergesort(left);
        right = mergesort(right);
        return merge(left, right);
    }

    private static LinkedList<Integer> merge(LinkedList<Integer> left, LinkedList<Integer> right) {
        // merge two already sorted lists
        LinkedList<Integer> merged = new LinkedList<>();
        while(!left.isEmpty() || !right.isEmpty()) {
            if(left.isEmpty()){
                merged.addAll(right);
                break;
            }
            if(right.isEmpty()){
                merged.addAll(left);
                break;
            }
            Integer e = left.peek() < right.peek() ? left.remove() : right.remove();
            merged.add(e);
        }
        return merged;
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
        System.out.println("mergesort: " + mergesort(u));
        System.out.println("Before qsort: "+ u);
        qsort(u, 0, u.size()-1);
        System.out.println("After qsort: " + u);
    }
}
