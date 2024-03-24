// Montoya Saiah
// CECS 342 Sec 7
// Bonus Assignment
// 10/19/2023
//Referenced from https://www.geeksforgeeks.org/tail-recursion-fibonacci/#

#include <iostream>
using namespace std;

// Tail recursive function to calculate n th fibonacci number
unsigned long long fib(int n, int a = 0, int b = 1)
{
    if (n == 0)
        return a;
    if (n == 1)
        return b;
    return fib(n - 1, b, a + b);
}

// Main
int main()
{
    unsigned long long n = 200;
    cout << "Fibonnaci of " << n << " = " << fib(n) << endl;
    return 0;
}