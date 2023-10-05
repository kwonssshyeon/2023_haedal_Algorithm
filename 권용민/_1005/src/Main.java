// 16236 아기상어
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[][] arr;
    static int[] dirR = {-1, 0, 0, 1};
    static int[] dirC = {0, -1, 1, 0};
    static class babyShark {
        int r;
        int c;
        int size = 2;
        int fishCount = 0;
        babyShark(int r, int c) {
            this.r = r;
            this.c = c;
        }
        int findClosestFish() {
            // r, c, travelTime
            Queue<Integer[]> queue = new LinkedList<>();
            Integer[] cur = {r, c, 0};
            queue.add(cur);

            boolean[][] visited = new boolean[N][N];
            visited[r][c] = true;

            while ((cur = queue.poll()) != null) {
                int curR = cur[0];
                int curC = cur[1];
                int travelTime = cur[2];
                //if (travelTime == Integer.MAX_VALUE)
                  //  break;

                // found!!!
                if (0 < arr[curR][curC] && arr[curR][curC] < this.size) {
                    // 같은 travelTime 걸리는 애들 다 poll
                    while ((cur = queue.poll()) != null && cur[2] == travelTime) {
                        if (0 < arr[cur[0]][cur[1]] && arr[cur[0]][cur[1]] < this.size &&
                                (cur[0] < curR || (cur[0] == curR && cur[1] < curC))) {
                            curR = cur[0];
                            curC = cur[1];
                        }
                    }
                    arr[curR][curC] = 0;
                    this.r = curR;
                    this.c = curC;
                    if (++this.fishCount == this.size) {
                        this.fishCount = 0;
                        this.size++;
                    }
                    return travelTime;
                }

                for (int dir = 0; dir < 4; ++dir) {
                    int nr = curR + dirR[dir];
                    int nc = curC + dirC[dir];
                    if (nr < 0 || nr >= N || nc < 0 || nc >= N
                        || visited[nr][nc]
                        || arr[nr][nc] > this.size)
                        continue;

                    queue.add(new Integer[]{nr, nc, travelTime + 1});
                    visited[nr][nc] = true;
                }
            }
            return 0;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        babyShark bs = null;
        arr = new int[N][N];
        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; ++j) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 9) {
                    bs = new babyShark(i, j);
                    arr[i][j] = 0;
                }
            }
        }

        int travelTime;
        int totalTravelTime = 0;
        while ((travelTime = bs.findClosestFish()) > 0) {
            totalTravelTime += travelTime;
        }

        System.out.println(totalTravelTime);
    }
}