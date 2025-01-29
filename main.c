//Recursive callstack

#include <stdio.h>

void countdown(int n) {
    printf("%d\n", n);

    if (n == 0) {
        return;
    }

    countdown(n - 1);
}

int main() {
    countdown(7);
    return 0;
}
