#!/usr/bin/env python3

import argparse

def extract(td):
    tdh=open(td, 'rb')
    tddata=tdh.read()
    tdh.close()

    jpegstart=b'\xff\xd8'
    jpegend=b'\xff\xd9'

    nextoffset=0;
    numfound=0;

    while True:
        print(f"debug: jpegstart={jpegstart}, type is {type(jpegstart)} AND nextoffset={nextoffset}, type is {type(nextoffset)}")
        nextstart=tddata.find(jpegstart, nextoffset)
        if nextstart<0:
            print("No more imgs found")
            break
        nextend=tddata.find(jpegend, nextstart)
        if nextend<0:
            print(f"Unfinished JPEG found")
            break

        numfound+=1;
        jpegdata=tddata[nextstart:nextend+1]
        jpegfile=open(f"output{numfound}.jpg", 'wb')
        jpegfile.write(jpegdata)
        jpegfile.close()
        nextoffset=nextend+2

def _main_():
    p=argparse.ArgumentParser(__file__)
    p.add_argument("-f", help="Android thumbdata file to extract images from")
    args=p.parse_args()
    print(f"extracting from {args.f}...")
    extract(args.f)


if __name__=="__main__":
    _main_()

