#include <stdio.h>
#include <stdlib.h>

int test()
{
    return 0;
}

int main()
{
    int a = test();
    int b = rand();
    int c = rand();
    return a * b;
}