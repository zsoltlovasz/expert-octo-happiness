#!/usr/bin/env python3

import argparse
import math

def check_prime(p, debug=False):
    if debug:
        print(f"running for {p} from 2 to {int(math.sqrt(p))}")
    for i in range(2, int(math.sqrt(p))+1):
        if debug: print(f"testing for remainder for {p} mod {i}")
        if p%i==0:
            if debug: print(f"{i} divides {p} without remainder so it's not prime")
            return False
    return True

def _main_():
    p=argparse.ArgumentParser(__file__)
    p.add_argument("-p", default=10, help="Mandatory argument to test")
    p.add_argument("-d", action="store_true", help="Turn on debugging")
    args=p.parse_args()
    print(f"calling check_prime with {int(args.p)} and {args.d} arguments")
    if check_prime(int(args.p), args.d):
        print(f"{args.p} is prime")
    else:
        print(f"{args.p} is NOT prime")

if __name__=="__main__":
    _main_()

