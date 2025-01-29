//Complejidad 1 O(n)

#include <stdio.h>
#include <stdbool.h>

bool linear_search(int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key) {
            return true;
        }
    }
    return false;
}

int main() {
    int test_n = 100;
    int test_arr[100];
    int test_key = 8;

    for (int i = 0; i < test_n; i++) {
        test_arr[i] = 7;
    }

    printf("%s\n", linear_search(test_arr, test_n, test_key) ? "true" : "false");

    return 0;
}


