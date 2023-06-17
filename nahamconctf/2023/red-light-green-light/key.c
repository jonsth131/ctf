#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;

    srand(7331u);
    
    for (i = 0LL; i != 32; ++i)
    {
        printf("%d, ", rand() % 62);
    }
}