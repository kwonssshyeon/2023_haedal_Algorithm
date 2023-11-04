// 11054 가장 긴 바이토닉 부분 수열
// DP
// 냅색처럼 다 2차원배열 만들 필요 없음

package org.example;

import java.util.Scanner;

public class Main {
    static final int UP = 0;
    static final int DOWN = 1;
    static int[] nums;
    static int[][] maxLengths;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        nums = new int[n];
        for (int i = 0; i < n; ++i)
            nums[i] = sc.nextInt();


        maxLengths = new int[n][2];
        for (int pre = 0; pre < n; ++pre) {
            for (int cur = pre + 1; cur < n; ++cur) {
                goWithStart(pre, cur);  // pre에서 부분수열 시작할 경우
                goWithUp(pre, cur);     // pre에서 증가하던 수열을 받아서 갈 경우
                goWithDown(pre, cur);   // pre에서 감소하던 수열을 받아서 갈 경우
            }
        }

        int maxLength = 1;
        for (int i = 0; i < n; ++i) {
            maxLength = Math.max(maxLength, maxLengths[i][UP]);
            maxLength = Math.max(maxLength, maxLengths[i][DOWN]);
        }

        System.out.println(maxLength);
    }

    static void goWithStart(int pre, int cur) {
        if (nums[pre] < nums[cur])  // 증가
            maxLengths[cur][UP] = Math.max(maxLengths[cur][UP], 2);
        else if (nums[pre] > nums[cur]) // 감소
            maxLengths[cur][DOWN] = Math.max(maxLengths[cur][DOWN], 2);
    }
    static void goWithUp(int pre, int cur) {
        if (maxLengths[pre][UP] == 0)
            return;

        if (nums[pre] < nums[cur])  // 증증
            maxLengths[cur][UP] = Math.max(maxLengths[cur][UP], maxLengths[pre][UP] + 1);
        else if (nums[pre] > nums[cur]) // 증감
            maxLengths[cur][DOWN] = Math.max(maxLengths[cur][DOWN], maxLengths[pre][UP] + 1);
    }
    static void goWithDown(int pre, int cur) {
        if (maxLengths[pre][DOWN] == 0)
            return;

        if (nums[pre] < nums[cur])  // 감증
            maxLengths[cur][UP] = Math.max(maxLengths[cur][UP], 2);
        else if (nums[pre] > nums[cur]) // 감감
            maxLengths[cur][DOWN] = Math.max(maxLengths[cur][DOWN], maxLengths[pre][DOWN] + 1);
    }
}
