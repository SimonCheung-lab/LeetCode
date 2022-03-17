int hammingWeight(uint32_t n) {
        /* 
        / 0000 0001 0010 0011 0100 0101 0110 0111 
        / 1000 1001 1010 1011 1100 1101 1110 1111
        */
        char table[] = {0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4}; 
        int count = 0;
        while (n)
        {
            count += table[n & 0xf];
            n = n >> 4;
        }
        return count;
}

// method 2
int hammingWeight(uint32_t n) {
    int count = 0;
    while (n)
    {
        // remove one bit
        n = n & (n - 1);
        count++;
    }
    return count;
}
