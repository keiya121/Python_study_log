#include<stdio.h>

typedef struct VECT3{
    double x[3];
}VECT3;

double dot_prod(VECT3 Vect3_1, VECT3 Vect3_2 );

int main()
{
    VECT3 p;
    VECT3 q;
    double ans;
    
    p.x[0] = 3.0; p.x[1] = 4.0; p.x[2] = 1.0;
    q.x[0] = 3.0; q.x[1] = 7.0; q.x[2] = 5.0;
    
    ans = dot_prod(p,q);
    
    printf("%f",ans);
    
    return 0;
    
}
double dot_prod( VECT3 Vect3_1, VECT3 Vect3_2 )
{
    double ans;
    
    ans = ((Vect3_1.x[0])*(Vect3_2.x[0]) + (Vect3_1.x[1])*(Vect3_2.x[1]) + (Vect3_1.x[2])*(Vect3_2.x[2]));
    
    return ans;
}