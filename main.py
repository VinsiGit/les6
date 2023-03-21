import rich
import sys
import os


def myping(host):
    response = os.system("ping -c 1 " + host)

    if response == 0:
        return True
    else:
        return False


print(myping("www.google.com"))
