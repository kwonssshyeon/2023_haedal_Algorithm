// DP랑 속도차이 엄청크진 않은데
// DP보다 위상정렬이 좀 더 빠르긴 한갑다
package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] buildingTimes;
    static int[] totalBuildingTimes;
    static int[] inDegrees;
    static List<Integer>[] nextNodeLists;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int test = Integer.parseInt(br.readLine());
        while (test-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            final int BUILDING_NUM = Integer.parseInt(st.nextToken());
            final int ORDER_NUM = Integer.parseInt(st.nextToken());

            buildingTimes = new int[BUILDING_NUM+1];
            totalBuildingTimes = new int[BUILDING_NUM+1];
            inDegrees = new int[BUILDING_NUM+1];
            nextNodeLists = new ArrayList[BUILDING_NUM + 1];
            for (int i = 1; i <= BUILDING_NUM; ++i)
                nextNodeLists[i] = new ArrayList<>();


            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= BUILDING_NUM; ++i)
                totalBuildingTimes[i] = buildingTimes[i] = Integer.parseInt(st.nextToken());

            for (int i = 0; i < ORDER_NUM; ++i) {
                st = new StringTokenizer(br.readLine());
                int building = Integer.parseInt(st.nextToken());
                int nextBuilding = Integer.parseInt(st.nextToken());
                nextNodeLists[building].add(nextBuilding);
                inDegrees[nextBuilding]++;
            }

            final int TARGET = Integer.parseInt(br.readLine());
            // 위상정렬
            Queue<Integer> q = new LinkedList<>();
            for (int i = 1; i <= BUILDING_NUM; ++i) {
                if (inDegrees[i] == 0)
                    q.offer(i);
            }
            while (!q.isEmpty()) {
                int node = q.poll();
                for (int nextNode : nextNodeLists[node]) {
                    totalBuildingTimes[nextNode] =
                            Math.max(totalBuildingTimes[nextNode], totalBuildingTimes[node] + buildingTimes[nextNode]);
                    inDegrees[nextNode]--;
                    if (inDegrees[nextNode] == 0)
                        q.offer(nextNode);
                }
                if (node == TARGET)
                    break;
            }

            System.out.println(totalBuildingTimes[TARGET]);
        }
    }
}
