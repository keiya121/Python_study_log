#include<stdio.h>
#include<math.h>

struct POINT {
    char name[5];
    double x;
    double y;
};

int main()
{
    int i;
    char tmp[5];
    struct POINT p[5];

    for (i=0; i<5; i++) {
        printf("%d番目の点の名前(5文字以内)とx座標,y座標を入力してください\n",i+1);
        printf("name:");
        scanf("%s",tmp);
        strcpy(p[i].name,tmp);
        printf("x:");
        scanf("%lf",&p[i].x);
        printf("y:");
        scanf("%lf",&p[i].y);
        printf("\n");
    }
    for (i=1; i<5; i++) {
        printf("%sと%sの距離は%fです。\n",p[0].name,p[i].name,sqrt((p[i].x-p[0].x)*(p[i].x-p[0].x)+(p[i].y-p[0].y)*(p[i].y-p[0].y)));
    }
    return 0;
}