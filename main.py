import sys
from functions import *

console = Console()

hostList = []
host = ""
ant = ""

if len(sys.argv) > 1:
    ant = sys.argv[1]
if len(sys.argv) > 2:
    hostList = sys.argv
    hostList.pop(0)
    hostList.pop(0)

if (len(sys.argv) < 2) and (len(hostList) == 0):
    console.print("What do you want to do?\n1.ping\n2.del\n3.show", style="bold")
    ant = input()
    if (ant == "ping") or (ant == "1") or (ant == "2") or (ant == "del"):
        host = input("What is the host: ")
        hostList.append(host)


if (ant == "ping") or (ant == "1"):
    for host in hostList:
        print(host)
        ping(host)
elif (ant == "del") or (ant == "2"):
    for host in hostList:
        delete(host)
elif ant == "show":
    show()

if ant == "" and host == "":
    pingAll()

website()
