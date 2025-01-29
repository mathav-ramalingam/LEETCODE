int smallestEvenMultiple(int n) {
    return (n%n==0 && n%2==0) ? n : n*2;
}