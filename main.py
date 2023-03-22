import sys
import os
import json
import rich
from functions import *

input = sys.argv[1]
host = sys.argv[2]

if input == "ping":
    myping(host)
elif input == "del":
    print(host)
    delete(host)


website()
