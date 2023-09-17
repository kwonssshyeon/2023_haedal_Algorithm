import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer>[] arr = new ArrayList[N+1];
        for (int i = 1; i <= N; ++i)
            arr[i] = new ArrayList<>();

        for (int i = 1; i < N; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            arr[s].add(e);
            arr[e].add(s);
        }

        int[] parent = new int[N+1];
        boolean[] visited = new boolean[N+1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        while(true) {
            var cur = queue.poll();
            if (cur == null)
                break;
            visited[cur] = true;

            arr[cur].forEach(e -> {
                if (!visited[e]) {
                    parent[e] = cur;
                    queue.add(e);
                }
            });
        }

        for (int i = 2; i <= N; ++i)
            System.out.println(parent[i]);
    }
}

/*
자바 진짜..........
귀찮고...느리고.....
에바다
*/
