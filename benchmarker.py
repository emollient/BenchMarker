"""
Author: Susan Lunn
I miss strict types :(
"""

import sys
import os
import subprocess
import time
import json
import argparse
import numpy


#sem = BoundedSemaphore

#returns a dict key = exec val = args
def program_args(args):
    execs = {}
    for i in range(len(args)-1):
        if args[i] == "-exec":
            i+=1
            curr_exec = args[i]
            execs.update({curr_exec:[]})
            while(i < len(args)-1 and args[i] != "-exec"):
                if(args[i] == "-arg"):
                   i+=1
                   execs[curr_exec].append(args[i])
                i+=1
            space = " "
            execs.update({curr_exec:space.join(execs[curr_exec])})

    return execs

"""
Runs each executable 30 times, 30 times
Computes the mean for each data set
returns {exec: mean}
"""
def aggregate(args):
    curr_dir = os.getcwd()
    data = {}
    times = {}


    for exece in args:
        for i in range(0,30):
            times.update({i:[]})
            for j in range(0,30):
                start = time.clock()
                subprocess.call("source "+curr_dir+"/"+exece+" "+args.get(exece)+ " > /dev/null 2>&1" , shell=True)
                times[i].append(time.clock()-start)

        data.update({exece:[]})
        for stat, stats in times.iteritems():
            data[exece].append(numpy.mean(stats))
        times = {}

    return data


#todo implement ability to run flags and thread
def main(argv):
    argv = program_args(argv[1:])
    stats = aggregate(argv)
    curr_dir = os.getcwd()

    with open("json.json" , "w") as file:
        json.dump(stats, file)

    subprocess.call("Rscript " + curr_dir+"/"+"benchmarkerANOVA.R",shell=True)


    #if(len(argv) <= 2):
    #    subprocess.call("R -f "+ curr_dir+"/"+"benchmarkerTtest.R", shell=True)
    #else:
    #    subprocess.call("R -f "+ curr_dir+"/"+"benchmarkerANOVA.R", shell=True)
    subprocess.call("rm json.json", shell=True)

if __name__ == "__main__" :
    main(sys.argv)












