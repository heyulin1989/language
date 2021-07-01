#include <stdio.h>

int x=11, y=12, sum, prod;
int subtract(void)
{
    __asm__(
            ".intel_syntax noprefix;"
            "mov rax,x;"
            "sub rax,y;"
            );
}

double add_float(float a, float b){
    return a + b;
}
double add_double(float a, float b)
{
    __asm__(
            ".intel_syntax noprefix;"
            "addsd xmm0, xmm1;"
            "movq rax, xmm0;"
            );
}

int add(int a, int b)
{
    __asm__(
            ".intel_syntax noprefix;"
            "mov rax, rdi;"
            "add rax, rsi;"
            );
}

int cpuid(long *e, long* d)
{
    __asm__(
            ".intel_syntax noprefix;"
            "xor r12, r12;"
            "mov rax, 1;"
            "cpuid;"
            "mov [rdi],rcx;"
            "mov [rsi],rdx;"
            );
    printf("ecx=%lx,edx=%lx\n",*e,*d);
    return 0;
}
int main()
{
    printf("The numbers are %d and %d\n", x, y);
    __asm__(
            ".intel_syntax noprefix;"
            "mov rax,x;"
            "add rax,y;"
            "mov sum,rax;"
            );
    printf("The sum is %d.\n",sum);
    printf("The difference is %d.\n",subtract());
    printf("The add is %d.\n",add(100,200));
    printf("The add float is %f.\n",add_float(100.12,200.12));
    long e,d;
    cpuid(&e,&d);
    return 0;
}
