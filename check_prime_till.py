#!/usr/bin/env python3

import check_prime

def check_till(limit=100):
    strlimit=str(limit)
    lower_limit=int(strlimit[:-1])
    for candidate in range(lower_limit, int(limit)+1):
        if check_prime.check_prime(candidate):
            print(f"check_till(): {candidate} is prime")
        #else:
        #    print(f"check_till(): {candidate} is NOT prime")

if __name__=="__main__":
    check_till(82818079787776757473727170696867666564636261605958575655545352515049484746454443424140393837363534333231302928272625242322212019181716151413121110987654322)

