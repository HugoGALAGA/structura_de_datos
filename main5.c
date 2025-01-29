//Stacks - stack
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int max;
    int top;
    char **elements;
} Stack;

void init_stack(Stack *stack, int size) {
    stack->max = size;
    stack->top = -1;
    stack->elements = (char **)malloc(size * sizeof(char *));
}

void free_stack(Stack *stack) {
    for (int i = 0; i <= stack->top; i++) {
        free(stack->elements[i]);
    }
    free(stack->elements);
}

void push(Stack *stack, const char *val) {
    if (stack->top == stack->max - 1) {
        printf("Stack overflow\n");
        return;
    }
    stack->top++;
    stack->elements[stack->top] = strdup(val);
}

char *pop(Stack *stack) {
    if (stack->top == -1) {
        printf("Stack underflow\n");
        return NULL;
    }
    char *val = stack->elements[stack->top];
    stack->elements[stack->top] = NULL;
    stack->top--;
    return val;
}

char *peek(Stack *stack) {
    if (stack->top == -1) {
        printf("Stack underflow\n");
        return NULL;
    }
    return stack->elements[stack->top];
}

void print_stack(Stack *stack) {
    printf("Current stack: [");
    for (int i = 0; i <= stack->top; i++) {
        printf("%s%s", stack->elements[i], (i < stack->top) ? ", " : "");
    }
    printf("] | Top: %d\n", stack->top);
}

int main() {
    Stack stack;
    init_stack(&stack, 5);

    push(&stack, "A");
    push(&stack, "B");
    print_stack(&stack);

    printf("Popped: %s\n", pop(&stack));
    print_stack(&stack);

    free_stack(&stack);
    return 0;
}