import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static class el {
        long num;
        int count;
        el(long num, int count) {
            this.num = num;
            this.count = count;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int ans = -2;
        int count = 1;
        Queue<el> queue = new LinkedList<>();
        queue.add(new el(a, count));
        el element;
        while((element = queue.poll()) != null) {
            a = element.num;
            count = element.count;
            if (a * 2 == b || a * 10 + 1 == b) {
                ans = count;
                break;
            }
            if (a * 2 < b)
                queue.add(new el(a * 2, count + 1));
            if (a * 10 + 1 < b)
                queue.add(new el(a * 10 + 1, count + 1));
        }

        System.out.println(ans+1);
    }
}
