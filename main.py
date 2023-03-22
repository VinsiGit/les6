import sys
import os
import json
from rich.console import Console
from functions import *

console = Console()

host = ""
ant = ""
if len(sys.argv) > 1:
    ant = sys.argv[1]
if len(sys.argv) > 2:
    host = sys.argv[2]

if len(sys.argv) < 2:
    console.print("What do you want to do?\nping\ndel\nshow", style="bold")
    ant = input()
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
