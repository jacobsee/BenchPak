# BenchPak

## Loop Parameter Detection
BenchPak repeatedly times the execution of a 2x2 matrix multiplication inside of a loop until it finds a loop size that takes over two seconds to run on the current machine. This is then used as a basis for later loop determinations. Loop parameter detection allows BenchPak to run in a reasonable amount of time regardless of the machine's performance, without modification.

## Usage
By default, BenchPak profiles matrix multiplication of square matrices from 2x2 to 2048x2048 using GCC's -O0, -O2, and -O3 optimization levels. The results are saved to a CSV file in the same directory as BenchPak. The matrix sizes and optimization levels can be adjusted in run.py.
