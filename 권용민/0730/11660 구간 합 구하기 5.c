#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[1024][1024];

int main()
{
	int n, m;
	int x1, y1, x2, y2;
	scanf("%d %d", &n, &m);
	
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			scanf("%d", &arr[i][j]);
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 1; j < n; ++j) {
			arr[i][j] += arr[i][j - 1];
		}
	}
	
	for (int i = 1; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			arr[i][j] += arr[i - 1][j];
		}
	}

	for (int i = 0; i < m; ++i) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		x1--;
		y1--;
		x2--;
		y2--;
		int sum = arr[x2][y2];
		if (x1 > 0)
			sum -= arr[x1 - 1][y2];
		if (y1 > 0)
			sum -= arr[x2][y1 - 1];
		if (x1 > 0 && y1 > 0)
			sum += arr[x1 - 1][y1 - 1];
		printf("%d\n", sum);
	}


	return 0;
}