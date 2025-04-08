
// Set of macros to manage exceptions in C with Longjump


void* quelque_part;

int foo(int in) {
    if (!in) goto quelque_part;
    return in + 10;
}

int bar(int a) {
    return foo(a);
}

int baz(int a) {
    return bar(a);
}

int main() {
    baz(42);

    FILE *fp = fopen("foo.txt","r");
    if (fp == NULL) {
        perror("fopen");
    }

}