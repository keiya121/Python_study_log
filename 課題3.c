#include <stdio.h>
#include <math.h>

typedef struct POINT{
  double x;
  double y;
} Point;

typedef struct LINE{
  Point s;
  Point e;
} Line;

void rotate_line( Line *a, double theta);

int main()
{
  Point p={0.0, 0.0}, q={1.0, 1.0};
  Line  a;
  double theta = M_PI/4.0;

  a.s = p;
  a.e = q;

  printf("始点の座標　(%f, %f)\n", a.s.x, a.s.y);
  printf("終点の座標　(%f, %f)\n", a.e.x, a.e.y);

rotate_line( &a, theta);

  printf("回転 %fラジアン\n", theta);
  printf("始点の座標　(%f, %f)\n", a.s.x, a.s.y);
  printf("終点の座標　(%f, %f)\n", a.e.x, a.e.y);

  return 0;
}

void rotate_line( Line *a, double theta)
{
    double tmp_s_x = a->s.x;
    double tmp_s_y = a->s.y;
    double tmp_e_x = a->e.x;
    double tmp_e_y = a->e.y;
    a->s.x = tmp_s_x*cos(theta) - tmp_s_y*sin(theta);
    a->s.y = tmp_s_x*sin(theta) + tmp_s_y*cos(theta);
    a->e.x = tmp_e_x*cos(theta) - tmp_e_y*sin(theta);
    a->e.y = tmp_e_x*sin(theta) + tmp_e_y*cos(theta);
}