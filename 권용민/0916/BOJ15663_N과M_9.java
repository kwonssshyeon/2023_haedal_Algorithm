import java.util.Arrays;
import java.util.Scanner;

public class BOJ15663_N과M_9 {
    static int n;
    static int m;
    static int[] arr;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; ++i)
            arr[i] = sc.nextInt();
        Arrays.sort(arr);

        int[] tmpArr = new int[m];
        boolean[] isChosen = new boolean[n];
        int[] lastPrintedInMyDigit = new int[m];
        func(tmpArr, 0, isChosen, lastPrintedInMyDigit);
    }

    public static void func(int[] tmpArr, int choosingDigit, boolean[] isChosen, int[] lastPrintedInMyDigit) {
        if (choosingDigit == m) {
            for (int i = 0; i < m; ++i)
                System.out.print(tmpArr[i] + " ");
            System.out.println();
            return;
        }

        for (int i = 0; i < n; ++i) {
            if (isChosen[i])
                continue;
            if (arr[i] == lastPrintedInMyDigit[choosingDigit])
                continue;
            tmpArr[choosingDigit] = lastPrintedInMyDigit[choosingDigit] = arr[i];
            isChosen[i] = true;
            func(tmpArr, choosingDigit + 1, isChosen, lastPrintedInMyDigit);
            for (int j = choosingDigit + 1; j < m; ++j) // arr 끝까지 돈 자리는 lastPrintedInMyDigit 초기화
                lastPrintedInMyDigit[j] = 0;
            isChosen[i] = false;
        }
    }
}
