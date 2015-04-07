import subprocess
import time

from shutil import move,copyfile
from os import remove,close
from tempfile import mkstemp

def main():
	print "\nBenchPak Matrix Multiply Performance Profiler"
	print "by Jacob See\n"
	print "Detecting appropriate loop parameters..."
	loop = detect_scale()
	print "Loop parameters set.\n"

	optimization_levels = [0,2,3]
	matrix_sizes = [2,4,8,16,32,64,128,256,512,1024]

	f = open("results.csv","w")
	f.write("BenchPak Results\n\n")
	f.write("Iterations,Matrix Size,Time (seconds)\n\n")

	for level in optimization_levels:
		curloop = loop
		print "Beginning work using optimization level " + str(level)
		f.write("Optimization Level " + str(level) + "\n")
		for matrix_size in matrix_sizes:
			print "\tNow testing: " + str(matrix_size)
			initnew()
			setparam("LENGTH",str(matrix_size))
			setparam("LOOP",str(curloop))
			compile(level)
			t = run()
			f.write(str(curloop) + "," + str(matrix_size) + "," + t + "\n")
			if curloop > 1:
				curloop /= 10
		f.write("\n")
	f.close()
	clean()

	print "\nFinished Testing!\n"

def detect_scale():
	loop = 100000
	total = 0
	while (total < 2):
		loop *= 10
		initnew()
		setparam("LENGTH","2")
		setparam("LOOP",str(loop))
		compile(0)
		t0 = time.time()
		run()
		total = time.time() - t0
	clean()
	return loop

def initnew():
	copyfile("specification.cpp","tmp.cpp")

def setparam(param, value):
	file_path = "tmp.cpp"
	fh, abs_path = mkstemp()
	with open(abs_path,'w') as new_file:
	    with open(file_path) as old_file:
	        for line in old_file:
	            new_file.write(line.replace("!["+param+"]", value))
	close(fh)
	remove(file_path)
	move(abs_path, file_path)

def compile(optimization_level):
	cmd = ["g++","-O"+str(optimization_level),"-std=c++11","tmp.cpp","-o","bin"]
	p = subprocess.Popen(cmd);
	p.wait();

def run():
	cmd = ["./bin"]
	p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
	p.wait()
	out = p.communicate()
	return out[0]

def clean():
	remove("tmp.cpp")
	remove("bin")

loop = 1
main()