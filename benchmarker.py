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
        subprocess.call(curr_dir+"/"+exece, shell=True)
        times.update({exece: time.clock() - start})

    #things are mutable and it confused me
    times = json.dumps(times)


    subprocess.call(curr_dir+"/"+"benchmarker.R", shell=True)

if __name__ == "__main__" :
    main(sys.argv)

