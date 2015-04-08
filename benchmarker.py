"""
Author: Susan Lunn
"""

import sys
import os
import gevent
import subprocess
import multiprocessing
import time
import json


#sem = BoundedSemaphore

def program_args(exece):
    yes = set(['yes', 'y', 'ye'])
    no = set(['no', 'n', ''])
    sys.stdout.write("Does %s require command-line arguments? [y/n] " % exece)
    yes_no = raw_input().lower()
    print( yes_no)
    if yes_no in no:
        return " "
    elif yes_no in yes:
        sys.stdout.write("Enter the command line arguments for %s: " % (exece))
        args = raw_input().lower()
        return " "+ args
    else:
        return program_args(exece)


#todo implement ability to run flags and thread
def main(argv):
    argv = argv[1:]
    times = {}
    start = time.clock()
    curr_dir = os.getcwd()
    print(curr_dir)
    for exece in argv:
        args = program_args(exece)
        times.update({exece: []})
        for i in range(0, 30):
            subprocess.call("./"+curr_dir+"/"+exece + args, shell=True)
            times[exece].append(time.clock() - start)

    with open("json.txt" , "w") as file:
        json.dump(times, file)



    if(len(argv) <= 2):
        subprocess.call("R -f "+ curr_dir+"/"+"benchmarkerTtest.R", shell=True)
    else:
        subprocess.call("R -f "+ curr_dir+"/"+"benchmarkerAnova.R", shell=True)
    subprocess.call("rm json.txt", shell=True)

if __name__ == "__main__" :
    main(sys.argv)

