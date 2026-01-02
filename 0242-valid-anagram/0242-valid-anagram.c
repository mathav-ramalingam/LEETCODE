#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isAnagram(char* s, char* t) {
    // Step 1: Check length
    if (strlen(s) != strlen(t))
        return false;

    int countS[26] = {0};
    int countT[26] = {0};

    // Step 2: Count characters
    for (int i = 0; s[i] != '\0'; i++) {
        countS[s[i] - 'a']++;
        countT[t[i] - 'a']++;
    }

    // Step 3: Compare frequency arrays
    for (int i = 0; i < 26; i++) {
        if (countS[i] != countT[i])
            return false;
    }

    return true;
}
