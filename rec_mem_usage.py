#!/usr/bin/python3

import os
import psutil
import argparse

def main():
    parser=argparse.ArgumentParser("Recursively counting memory usage of a process and all its children")
    parser.add_argument("-p", default=1, help="pid of the parent process of the tree")
    args=parser.parse_args()
    ppid=int(args.p)
    ppr=psutil.Process(ppid)
    mem=ppr.memory_percent()
    numpr=1
    for chpr in ppr.children(recursive=True):
        mem+=chpr.memory_percent()
        numpr+=1
    print(f"Total memory usage for pid {ppid} is {mem}, found in total {numpr} processes")

if __name__ == "__main__":
    main()
