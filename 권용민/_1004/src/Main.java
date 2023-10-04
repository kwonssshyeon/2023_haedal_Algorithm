import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long[] arrR = new long[n];
        long[] arrC = new long[n];
        for (int i =0; i < n; ++i) {
            st = new StringTokenizer(br.readLine());
            arrR[i] = Long.parseLong(st.nextToken());
            arrC[i] = Long.parseLong(st.nextToken());
        }

        long sumA = 0;
        long sumB = 0;
        for (int i = 0; i < n; ++i) {
            sumA += arrR[i] * arrC[(i+1) % n];
            sumB += arrR[(i+1) % n] * arrC[i];
        }
        System.out.printf("%.1f", Math.abs(Math.round((sumA - sumB) / 2.0 * 10) / 10.0));
    }
}