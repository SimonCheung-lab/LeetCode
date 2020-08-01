double myPow(double x, int n){
    if (n == 0) {
        return 1;
    }

    if (n < 0) {
        if (n > -2147483648){
            return 1.0 / myPow(x, -n);
        }
        else {
            return 1.0 / (x * myPow(x, 2147483647));
        }
    }

    if (n % 2 == 0) {
        return myPow(x * x, n / 2);
    }

    return x * myPow(x, n - 1);
}
