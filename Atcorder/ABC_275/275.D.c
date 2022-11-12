#include <stdio.h>
int cul(int a){
    if (a == 0){
        return 1;
    }
    return (cul(a/2) + cul(a/3));
}
int main(void){
    long long int ans;
    long long int N;

    scanf("%lld",&N);
    ans = cul(N);
    printf("%lld",ans);
    return 0;
}

