#include<stdio.h>
#include<stdlib.h>

#define SIZE 5
#define TRUE 1
#define FALSE 0

struct stack {
    int TOP;
    int Item[SIZE];
};

struct stack S;

void Initalize(void) {
    S.TOP = -1;
}

int Empty(void) {
    if (S.TOP == -1)
        return TRUE;
    else
        return FALSE;
}

void Push(int x) {
    if (S.TOP == SIZE - 1) {
        printf("stack overflow");
        exit(1);
    }
    S.TOP = S.TOP + 1;
    S.Item[S.TOP] = x;
    printf("\n%d was pushed into the stack.", x);
}

int Pop() {
    int x;
    if (Empty()) {
        printf("stack underflow");
        exit(1);
    }
    x = S.Item[S.TOP];
    S.TOP = S.TOP - 1;
    return x;
}

void main() {
    Initalize();
    int x;
    Push(100);
    Push(200);
    Push(300);
    Push(400);
    Push(500);
    x = Pop();
    printf("\n%d was popped from the stack.", x);
    x = Pop();
    printf("\n%d was popped from the stack.", x);
    x = Pop();
    printf("\n%d was popped from the stack.", x);
}
