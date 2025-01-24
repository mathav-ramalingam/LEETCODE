int countPrimes(int n) {

    if (n < 2) 
    {
        return 0; 
    } 

    // Using Sieve of Eratosthenes
    int arr[n];

    for (int i = 0; i < n; i++) 
    {
        arr[i] = i; 
    }
    arr[0] = arr[1] = 0; 

    for (int p = 2; p * p < n; p++) 
    {
        if (arr[p] != 0) 
        { 
            for (int i = p * p; i < n; i += p) 
            {
                arr[i] = 0; 
            }
        }
    }


    int count = 0;
    for (int i = 2; i < n; i++) 
    {
        if (arr[i] != 0) 
        {
            count++;
        }
    }

    return count; 
}
