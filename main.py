import sys
import os
import json
import rich
from functions import *

host = ""
ant = ""
if len(sys.argv) > 1:
    ant = sys.argv[1]
if len(sys.argv) > 2:
    host = sys.argv[2]

if len(sys.argv) < 2:
    ant = input("What do you want to do?\nping\ndel\nshow\n")
    if (ant == "ping") or (ant == "del"):
        host = input("What is the host: ")


if ant == "ping":
    ping(host)
elif ant == "del":
    delete(host)
elif ant == "show":
    show()

if ant == "" and host == "":
    pingAll()

website()
