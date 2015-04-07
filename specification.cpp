#include <iostream>
#include <chrono>
#include <vector>
#include <random>

#define LOOP ![LOOP]
#define LENGTH ![LENGTH]

using namespace std;

int main()
{
	
	uniform_real_distribution<double> rndgen(0.0, 100.0);

	default_random_engine r(chrono::system_clock::now().time_since_epoch().count());

	double **a = new double*[LENGTH];
	double **b = new double*[LENGTH];
	double **c = new double*[LENGTH];
	for (int i = 0; i < LENGTH; i++)
	{
		a[i] = new double[LENGTH];
		b[i] = new double[LENGTH];
		c[i] = new double[LENGTH];
	}

	for (int i = 0; i < LENGTH; i++)
	{
		for (int j = 0; j < LENGTH; j++)
		{
			a[i][j] = rndgen(r);
			b[i][j] = rndgen(r);
			c[i][j] = 0;
		}
	}

	//cout << "Matrix Multiply Benchmark" << endl << "CSCE 448 --- Jacob See" << endl << endl;
	int res = chrono::high_resolution_clock::period::den;
	//cout << "Current machine's high-resolution clock rate: " << endl << res << " ticks / sec." << endl << "Now running..." << endl << endl;

	auto start_time = chrono::high_resolution_clock::now();

	for (int l = 0; l < LOOP; l++)
	{
		for (int i = 0; i < LENGTH; i++)
		{
			for (int n = 0; n < LENGTH; n++)
			{
				for (int x = 0; x < LENGTH; x++)
				{
					c[i][n] += a[i][x] * b[x][n];
				}
			}
		}
	}

	auto end_time = chrono::high_resolution_clock::now();
	double duration = (double)chrono::duration_cast<chrono::microseconds>(end_time - start_time).count();
/*
	long ops = (LENGTH * LENGTH * LENGTH) + ((LENGTH - 1) * LENGTH * LENGTH);
	cout << "Iterations: " << LOOP << endl;
	cout << "Matrix Size (N x N): " << LENGTH << endl;
	cout << "Total Elapsed Time: " << duration / 1000000.0 << " seconds." << endl;
	cout << "Average Time Per Matrix: " << (double)duration / LOOP << " microseconds." << endl;
	cout << "FLOPS: " << ops / (duration / 1000000.0) << endl;
*/
	cout << duration / 1000000.0;

	return 0;
}