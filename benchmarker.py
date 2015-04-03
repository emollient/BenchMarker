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


#todo implement ability to run flags and thread
def main(argv):
    argv = argv[1:]
    times = {}
    start = time.clock()
    curr_dir = os.getcwd()
    print(curr_dir)
    for exece in argv:
        times.update({exece: []})
        for i in range(0, 30):
            subprocess.call("source "+curr_dir+"/"+exece, shell=True)
            times[exece].append(time.clock() - start)

    with open("json.txt" , "w") as file:
        json.dump(times, file)


    subprocess.call("R -f "+ curr_dir+"/"+"benchmarker.R", shell=True)
    #subprocess.call("rm json.txt", shell=True)

if __name__ == "__main__" :
    main(sys.argv)

