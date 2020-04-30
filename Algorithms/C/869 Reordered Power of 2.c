int length(int n)
{
    int len = 0;
    do {
        ++len;
        n /= 10;
    } while(n);
    return len;
}

bool match(int N, int i)
{
    int M = pow(2, i);
    int len_M = length(M);
    int len_N = length(N);
    if (len_M != len_N){
        return false;
    }

    int counter[10];
    memset(counter, 0, 10 * sizeof(int));

    do {
        ++counter[M % 10];
        M /= 10;
    } while(M);

    do {
        if (--counter[N % 10] < 0) {
            return false;
        }
        N /= 10;
    } while (N);

    for (int j = 0; j < 10; ++j){
        if (counter[j] != 0) {
            return false;
        }
    }

    return true;
}

bool reorderedPowerOf2(int N){
    for (int i = 0; i < 32; ++i){
        if (match(N, i)){
            return true;
        }
    }

    return false;
}
