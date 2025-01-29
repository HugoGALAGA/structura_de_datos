//Stacks - OOP
#include <stdio.h>
#include <string.h>

typedef struct {
    char model[50];
    int kms;
} Car;

void init_car(Car *car, const char *model, int kms) {
    strcpy(car->model, model);
    car->kms = kms;
}

void print_car(const Car *car) {
    printf("Modelo: %s | KM: %d\n", car->model, car->kms);
}

void broom(Car *car, int distance) {
    car->kms += distance;
}

int main() {
    Car daily;
    init_car(&daily, "Porsche 911", 0);
    print_car(&daily);
    broom(&daily, 50);
    print_car(&daily);

    return 0;
}