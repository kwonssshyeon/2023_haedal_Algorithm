import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] dirR = { -1, 1, 0, 0 };
    static int[] dirC = { 0, 0, -1, 1 };

    public static int[] getBestPlace(int n, int[][] arr, int[] myLikeArr) {
        int maxLikeCount = 0;
        int bestR = 0;
        int bestC = 0;
        int maxEmptyCount = 0;

        // getCurLikeCount per cell
        for (int r = 1; r <= n; ++r) {
            for (int c = 1; c <= n; ++c) {
                // 이미 자리있으면
                if (arr[r][c] > 0)
                    continue;
                // 주변에 좋아하는 애 or 빈자리 아무것도 없는 케이스 대비 
                if (bestR == 0) {
                    bestR = r;
                    bestC = c;
                }

                int curLikeCount = 0;
                int curCloseEmptyCount = 0;

                // 사방 탐색
                for (int dirIdx = 0; dirIdx < 4; ++dirIdx) {
                    int nr = r + dirR[dirIdx];
                    int nc = c + dirC[dirIdx];
                    if (nr < 1 || nr > n || nc < 1 || nc > n)
                        continue;

                    // 비었으면
                    if (arr[nr][nc] == 0) {
                        curCloseEmptyCount++;
                        continue;
                    }
                    // 내 like면
                    for (int likeIndex = 1; likeIndex < 5; ++likeIndex) {
                        if (arr[nr][nc] == myLikeArr[likeIndex]) {
                            curLikeCount++;
                            break;
                        }
                    }
                }

                // 좋아하는 사람 더많은 곳 발견
                if (maxLikeCount < curLikeCount)
                {
                    maxLikeCount = curLikeCount;
                    bestR = r;
                    bestC = c;
                    maxEmptyCount = curCloseEmptyCount;
                }
                // 좋아하는 사람은 같은데 빈자리 더 많은 곳 발견
                else if (maxLikeCount == curLikeCount && maxEmptyCount < curCloseEmptyCount)
                {
                    bestR = r;
                    bestC = c;
                    maxEmptyCount = curCloseEmptyCount;
                }
            }
        }

        int[] res = { bestR, bestC };
        return res;
    }

    public static int checkEveryHappyCount(int n, int[][] arr, int[][] likeArr) {
        int studentN = n * n;
        int sum = 0;
        // 모든 학생에 대해
        for (int r = 1; r <= n; ++r) {
            for (int c = 1; c <= n; ++c) {
                int myLikeCount = 0;

                int[] myLikeArr = likeArr[0];
                for (int studentIdx = 0; studentIdx < studentN; ++studentIdx) {
                    if (likeArr[studentIdx][0] == arr[r][c]) {
                        myLikeArr = likeArr[studentIdx];
                        break;
                    }
                }

                for (int dirIdx = 0; dirIdx < 4; ++dirIdx) {
                    int nr = r + dirR[dirIdx];
                    int nc = c + dirC[dirIdx];

                    if (nr < 1 || nr > n || nc < 1 || nc > n)
                        continue;
                    for (int i = 1; i < 5; ++i) {
                        if (myLikeArr[i] == arr[nr][nc]) {
                            myLikeCount++;
                            break;
                        }
                    }
                }

                switch(myLikeCount) {
                    case 1:
                        sum += 1;
                        break;
                    case 2:
                        sum += 10;
                        break;
                    case 3:
                        sum += 100;
                        break;
                    case 4:
                        sum += 1000;
                }
            }
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        int studentN = n * n;
        int[][] likeArr = new int[studentN][5];
        for (int i = 0; i < studentN; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; ++j) {
                int likeStudent = Integer.parseInt(st.nextToken());
                likeArr[i][j] = likeStudent;
            }
        }

        int[][] arr = new int[n+1][n+1];
        for (int likeArrIndex = 0; likeArrIndex < studentN; ++likeArrIndex) {
            int[] myLikeArr = likeArr[likeArrIndex];
            int me = myLikeArr[0];

            int[] bestPlace = getBestPlace(n, arr, myLikeArr);
            int bestR = bestPlace[0];
            int bestC = bestPlace[1];
            arr[bestR][bestC] = me;
        }

        System.out.println(checkEveryHappyCount(n, arr, likeArr));
    }
}
