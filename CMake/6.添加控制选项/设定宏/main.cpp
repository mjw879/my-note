#include<stdio.h>
int main()
{
#ifdef myDefine1
    printf("myDefine1\n");
#endif
#ifdef myDefine2
    printf("myDefine2\n");
#endif

    return 0;
}
