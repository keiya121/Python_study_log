#include <stdio.h>
int cul(int a){
    if (a == 0){
        return 1;
    }
    return (cul(a/2) + cul(a/3));
}
int main(void){
    int ans;
    int N;

    scanf("%d",&N);
    ans = cul(N);
    printf("%d",ans);
    return 0;
}

