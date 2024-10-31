#include <stdio.h>
int globalvar = 10;

int main()
{
	int a = 1;
	int b = a + 1;
	printf("%d",b+globalvar);
}

