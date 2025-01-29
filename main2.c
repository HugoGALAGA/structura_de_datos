//Complejidad O(n^2)
#include <stdio.h>
#include <stdbool.h>

bool product_in_list(int arr[], int size, int product) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (arr[i] * arr[j] == product) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    int test_n = 100;
    int test_arr[100];
    int test_product = 1;

    for (int i = 0; i < test_n; i++) {
        test_arr[i] = 1;
    }

    printf("%s\n", product_in_list(test_arr, test_n, test_product) ? "true" : "false");

    return 0;
}
