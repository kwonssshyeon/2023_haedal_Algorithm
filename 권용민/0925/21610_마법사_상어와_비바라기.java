import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] dirR = {9999999, 0, -1, -1, -1, 0, 1, 1, 1};
    static int[] dirC = {9999999, -1, -1, 0, 1, 1, 1, 0, -1};
    static int[][] arr;
    static boolean[][] cloudArr;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N + 1][N + 1];
        cloudArr = new boolean[N + 1][N + 1];
        for (int i = 1; i <= N; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; ++j) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        cloudArr[N][1] = cloudArr[N][2] = cloudArr[N - 1][1] = cloudArr[N - 1][2] = true;
        for (int i = 0; i < M; ++i) {
            st = new StringTokenizer(br.readLine());
            int dirIdx = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            cloudArr = moveClouds(dirIdx, dist);
            makeRain();
            copyWaterMagic();
            cloudArr = makeCouds();
        }

        System.out.println(getWaterAmounts());
    }

    public static boolean[][] moveClouds(int dirIdx, int dist) {
        boolean[][] nextClouds = new boolean[N + 1][N + 1];
        for (int r = 1; r <= N; ++r) {
            for (int c = 1; c <= N; ++c) {
                if (cloudArr[r][c] == false)
                    continue;

                int nr = r;
                int nc = c;
                for (int i = 0; i < dist; ++i) {
                    nr += dirR[dirIdx];
                    nc += dirC[dirIdx];
                    if (nr == 0)
                        nr = N;
                    else if (nr == N + 1)
                        nr = 1;
                    if (nc == 0)
                        nc = N;
                    else if (nc == N + 1)
                        nc = 1;
                }
                nextClouds[nr][nc] = true;
            }
        }
        return nextClouds;
    }

    public static void makeRain() {
        for (int r = 1; r <= N; ++r) {
            for (int c = 1; c <= N; ++c) {
                if (cloudArr[r][c])
                    arr[r][c]++;
            }
        }
    }

    public static void copyWaterMagic() {
        int[] dirDiagR = {-1, -1, 1, 1};
        int[] dirDiagC = {-1, 1, 1, -1};
        for (int r = 1; r <= N; ++r) {
            for (int c = 1; c <= N; ++c) {
                if (cloudArr[r][c] == false)
                    continue;
                for (int i = 0; i < 4; ++i) {
                    int nr = r + dirDiagR[i];
                    int nc = c + dirDiagC[i];
                    if (nr < 1 || nc < 1 || nr > N || nc > N || arr[nr][nc] == 0)
                        continue;
                    arr[r][c]++;
                }
            }
        }
    }

    public static boolean[][] makeCouds() {
        boolean[][] nextClouds = new boolean[N + 1][N + 1];

        for (int r = 1; r <= N; ++r) {
            for (int c = 1; c <= N; ++c) {
                if (cloudArr[r][c] || arr[r][c] < 2)
                    continue;
                arr[r][c] -= 2;
                nextClouds[r][c] = true;
            }
        }

        return nextClouds;
    }

    public static int getWaterAmounts() {
        int sum = 0;
        for (int r = 1; r <= N; ++r) {
            for (int c = 1; c <= N; ++c) {
                sum += arr[r][c];
            }
        }
        return sum;
    }
}
