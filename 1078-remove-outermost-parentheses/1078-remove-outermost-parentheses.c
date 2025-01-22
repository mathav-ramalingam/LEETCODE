#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* removeOuterParentheses(char* S) {
    
    int len = strlen(S);
    char* ans = (char*)malloc(len * sizeof(char)); 
    int ansIndex = 0;
    int openCount = 0;           // To count opening parentheses
    
    for (int i = 0; i < len; i++) {
        if (S[i] == '(') {
            if (openCount > 0)    // Skip the first '('
            {  
                ans[ansIndex++] = S[i];  // Add '(' to result
            }
            openCount++;  // Increment for '('
        } 
        else if (S[i] == ')')
         {
            openCount--;  // Decrement for ')'
            if (openCount > 0) // Skip the last ')'
            {  
                ans[ansIndex++] = S[i];  // Add ')' to result
            }
        }
    }
    
    ans[ansIndex] = '\0';  // Null-terminate the result string
    return ans;
}