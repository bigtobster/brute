#!/usr/bin/env python3

# Will attempt infinite passwords for a Zip.
# Assumes that the password used is ASCII
# Makes no attempt to try common or human friendly passwords first
# Generator based so highly memory efficient
# Single threaded so scales with CPU hz

from zipfile import ZipFile
import string, itertools, sys, os

def hackZip(target, pwd):
    try:
        with ZipFile(target, "r") as myZip:
            myZip.extractall(pwd=pwd)
            print(target, "hacked with password", pwd)
    except Exception as e:
        print("Hack failed with pass '{}'".format(pwd))
        raise e

def genPass():
    chars = string.printable
    # Goes for infinity (or until user aborts)
    for length in itertools.count(start=1):
        for pwd in itertools.permutations(chars, length):
            yield "".join(pwd)

def brute(target):
    passGen = genPass()
    for pwd in passGen:
        try:
            hackZip(target, pwd)
        except:
            pass

if __name__ == "__main__":
    path = sys.argv[1]
    if not os.path.exists(path):
        print(path, "does not exist")
        sys.exit()
    if not path[-4:] == ".zip":
        print(path, "is not a Zip file")
        sys.exit()
    brute(path)
    print("Zip Hacked")


