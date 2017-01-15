import os
import sys
import timeit
import statistics

record_time = open(sys.argv[3],'w')

num_runs = int(sys.argv[1])
program = sys.argv[2]

num = 5
num_orig = 1
elapsed_time = []
for i in range(1,num_runs+1):
	record_time.write('run number:')
	record_time.write(str(i))
	record_time.write("\n")
	start_time = timeit.default_timer()
	if program == "spec.da":
		os.system("dar " + program + " 3 3 3 1 "+str(num))
	elif program == "orig.da":
		os.system("dar " + program + " 3 3 2 1 "+str(num_orig))
	else:
		os.system("dar " + program + " 3 3 2 "+str(num))
	num = num + 5
	num_orig = num_orig + 5
	elapsed = timeit.default_timer() - start_time
	elapsed_time.append(elapsed)
	record_time.write("time taken by this run: ")
	record_time.write(str(elapsed))
	record_time.write("\n")

record_time.write("mean:")
record_time.write(str(statistics.mean(elapsed_time)))
record_time.write("\n")
record_time.write("median:")
record_time.write(str(statistics.median(elapsed_time)))
record_time.write("\n")
record_time.close()