#include <stdio.h>

int main(void) {
    int a[6] = {0};

    int i;              // uninitialized
    a[i] = 1;           // use uninitialized i

    {
        int i;      // different variable (shadowing), initialized
        a[i] = 3;       // fine, but helps test scoping
    }

    printf("%d\n", a[2]);
    return 0;
}
