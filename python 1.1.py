
#include <stdio.h>
 
// Recursive function to calculate factorial of a number
unsigned long factorial(int n)
{
    // base case: if `n` is 0 or 1
    if (n < 1) {
        return 1;
    }
 
    // use the recurrence relation
    return n * factorial(n - 1);
}
 
int main()
{
    int n = 5;
    printf("The Factorial of %d is %lu", n, factorial(n));
 
    return 0;
}

The Factoria

Java
Python
The time complexity of the above solution is O(n), and the auxiliary space used by the program is O(n) fo
#include <stdio.h>
 
// Recursive function to calculate factorial of a number
unsigned long factorial(int n) {
    return (n < 1) ? 1 : n * factorial(n - 1);
}
 
int main()
{
    int n = 6;
    printf("The Factorial of %d is %lu", n, factorial(n));
 
    return 0;
}
Download  Run Code

Output:

The Factorial of 6 is 720

Java
Python
 
Also see:

Iterative program to find factorial of a number

 
Exercise: Efficiently print factorial series in a given range.

Rate this post

Average rating 4.79/5. Vote count: 157


Last Reviewed By: Admin
Previous:Find all factorial numbers less than or equal to nNext:Iterative solution to reverse a string in C++ and Java


