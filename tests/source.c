#include <stdio.h>

int function1() {
    printf("you are calling function1: %p\n", &function1);
};
int function2() {
    printf("you are calling function2: %p\n", &function2);
};
int function3() {
    printf("you are calling function3: %p\n", &function3);
};
int main() {
    function1();
    function2();
    function3();
};
