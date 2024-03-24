//Saiah Montoya
//CECS 342
//Prog 1 Fibonacci Race
//9/12/23
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
using namespace std;
#include <ctime>
// Fibo function

long long fibo(int n)
{
    if (n == 1 || n == 0)
        return 1;
    else
        return fibo(n-1) + fibo(n-2);
}
int main()
{
    for (int i = 1; i <= 50; i++)
    {
        clock_t start_time = clock();
        long long result = fibo(i);
        clock_t end_time = clock();

        double t = static_cast<double>(end_time - start_time) / CLOCKS_PER_SEC;
        cout << i << ":" << result << " Time taken: "<< t <<endl;
    }
    return 0;
}

// time 0, capture, time 0 again, take difference;