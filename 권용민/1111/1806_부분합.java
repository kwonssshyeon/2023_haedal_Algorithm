// 예외처리가 좀 지저분하긴 한디.. 피곤허다
package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int s = scanner.nextInt();
        int start = 0;
        int sum = 0;
        int minLen = Integer.MAX_VALUE;
        int curLen = 0;


        if (s == 0) {
            System.out.println(1);
            return;
        }
        int[] arr = new int[n];
        for (int i = 0; i < n; ++i) {
            arr[i] = scanner.nextInt();
            sum += arr[i];
            curLen++;
            if (sum >= s) {
                while (sum >= s) {
                    sum -= arr[start++];
                    curLen--;
                }
                minLen = Math.min(minLen, curLen+1);
            }
        }

        if (minLen == Integer.MAX_VALUE)
            System.out.println(0);
        else
            System.out.println(minLen);
    }
}
