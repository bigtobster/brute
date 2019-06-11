# A simple ZIP brute forcer
Only works on zips and the zip must have the extension ".zip".
Written in Python 3
Extremely compute intensive on a single core. Single cored machines BEWARE!
Not multi-threaded so should be fine on any multi-core PC
To cancel, simple Ctrl-C or Kill the job from a job manager
Works on all environments where Python does
It will try an infinite series of passwords with no bias to human-friendliness
It executes in length and ASCII order
Note that for non-trivial passwords (i.e. 6 characters or more), this will take HOURS/DAYS/WEEKS depending on your core performance

## Installation
Should be easy as pie. It only depends on stdlib for Python 3 so should work anywhere.
Simply download brute.py
To execute in bash, you must first run chmod +x brute.py

## Usage
### From Python
import brute
brute.brute(pathToZip

### From Bash
./brute.py pathToZip



