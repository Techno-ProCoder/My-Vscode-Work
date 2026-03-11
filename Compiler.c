#include <stdio.h>
struct stud
{
    int rollno;
    char name[20];
};
struct stud s[3];
int main()
{
    int n;
    struct stud *p=s;
    printf("Please Enter No. Of Records");
    scanf("%d", &n);
    while(p<s+n)
    {
        scanf("%d%s", &p->rollno, p->name);
        p++;
    }
    p=s;
    while(p<s+n)
    {
        printf("%d %s", p->rollno, p->name);
        p++;
    }
}