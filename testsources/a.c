#include <stdio.h>

int main(void) {
    int a[8] = {0};
	int i;
	a[0] = a[i]; // wrong subscript expr => not lvalue, but rvalue
//	a[0] = a[i=1]; // 이건 ㄱㅊ. i가 lvalue라 assign 가능.
}
