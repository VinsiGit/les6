import sys
import os
import json

data = {}

host = sys.argv[1]


def myping(host):
    response = os.system("ping -c 1 " + host)

    if response == 0:
        data[host] = True
        print("did work")
    else:
        data[host] = False
        print("did not work")
    json.dumps(data)


myping(host)
# myping("www.google.com")
print(data)
