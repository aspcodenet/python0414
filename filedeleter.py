#pip install argparse

#python filedeleter.py -d c:\temp\test -s 50000
#python filedeleter.py -d c:\temp\test --size 50000
from argparse import ArgumentParser
import os

argParser = ArgumentParser() 
argParser.add_argument("-s", "--size", help="min size of files to delete", type=int, default=50000) 
argParser.add_argument("-d", "--directory", help="directory", type=str) 
args = argParser.parse_args() 


for filename in os.scandir(args.directory):
    if filename.is_file():
        if os.path.getsize(filename.path) > args.size:
            print("removing " + filename.path)
            os.remove(filename.path)



