import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    final static int DIRTY = 0;
    final static int WALL = 1;
    final static int CLEANED = 2;
    final static int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    // N, E, S, W
    public static boolean isThereDirty(int[][] arr, int n, int m, int r, int c) {
        if (r > 0 && arr[r-1][c] == DIRTY ||
            c > 0 && arr[r][c-1] == DIRTY ||
            r < n - 1 && arr[r+1][c] == DIRTY ||
            c < m - 1 && arr[r][c+1] == DIRTY)
            return true;
        return false;
    }

    public static int turnLeft(int frontIdx) {
        return (frontIdx + 4 - 1) % 4;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n =  Integer.parseInt(st.nextToken());
        int m =  Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int r =  Integer.parseInt(st.nextToken());
        int c =  Integer.parseInt(st.nextToken());
        int frontIdx =  Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][m];
        for (int i =0; i < n; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; ++j) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 0: dirty, 1: wall, 2: cleaned
        int cleanCount = 0;
        int nr, nc;
        while (true) {
            if (arr[r][c] == DIRTY) {
                arr[r][c] = CLEANED;
                cleanCount++;
            }
            if(isThereDirty(arr, n, m, r, c)) {
                do {
                    frontIdx = turnLeft(frontIdx);
                    nr = r + directions[frontIdx][0];
                    nc = c + directions[frontIdx][1];
                } while (nr < 0 || nc < 0 || nr >= n || nc >= m || arr[nr][nc] != DIRTY);
                // move front
                r = nr;
                c = nc;
            } else {
                nr = r + directions[(frontIdx + 2) % 4][0];
                nc = c + directions[(frontIdx + 2) % 4][1];
                // move back
                if (arr[nr][nc] != WALL) {
                    r = nr;
                    c = nc;
                } else {
                    break;
                }
            }
        }

        System.out.println(cleanCount);
    }
}
