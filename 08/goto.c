
int processing(int data) {
    int error = 0;
    void *space = malloc(1024);
    
    if (data < 42) {
        error = 2;
        goto error;
    }

    if (data > 108) {
        error = 1;
        goto error;
    }
    
  error: 
    free(space);
    return error;
}