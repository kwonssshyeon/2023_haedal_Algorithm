#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	unsigned long long ans = 1;
	int squareCount = 1;

	/*
	11 => 1011
	1 2 4 8 + 1 2 + 1 
	*/
	while (b) 
	{
		unsigned long long tmp = a;
		if (b & 1) {
			for (int i = 1; i < squareCount; ++i) {
				tmp *= tmp;
				tmp %= c;
			}
			ans *= tmp;
			ans %= c;
		}
		squareCount++;
		b >>= 1;
	}
	printf("%llu", ans);

	return 0;
}
