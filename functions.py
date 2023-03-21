import sys
import os
import json
import rich


def myping(host):
    response = os.system("ping -c 1 " + host)
    data = ""
    check = {}
    with open("bestand.json", "r") as f:
        check = json.load(f)
    if response == 0:
        data = "True"
        print("did work")
    else:
        data = "False"
        print("did not work")
    print(check)
    change = False
    for k, v in check.items():
        print(k, v)
        print(host, data)
        if (k != host) or (v != data):
            change = True
            print("work")
    if change:
        check[host] = data

    print(check)

    with open("bestand.json", "w") as f:
        json.dump(check, f, indent=2)


def website():
    template = open("template.html", "r")
    html = template.read()
    with open("bestand.json", "r") as f:
        data = json.load(f)
    print(data)
    i = []
    for k in data:
        print(k)
        i.append(k)
    print(i)
    i = str(i)
    i = i.replace("'", "")
    i = i.replace(",", "")
    i = i.replace("]", "")
    i = i.replace("[", "")
    html = html.replace("X", i)
    for k, v in data.items():
        data = f"<br>{k}: {v}"
        html = html.replace(k, data)
    template.close()

    index = open("index.html", "w")
    index.write(html)
    index.close()
