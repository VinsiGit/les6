import os
import json
import re
from rich.console import Console

console = Console()


def ping(host):
    """
    host -> ping\n
    sends a ping to the host and stores the answer in a json
    """
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
    # print(check)
    change = False
    for k, v in check.items():
        # print(k, v)
        # print(host, data)
        if (k != host) or (v != data):
            change = True
            # print("work")
    if change:
        check[host] = data
    if not check:
        check[host] = data
    # print(check)

    with open("bestand.json", "w") as f:
        json.dump(check, f, indent=2)


def website():
    """
    makes the website
    """
    template = open("website/template.html", "r")
    html = template.read()
    with open("bestand.json", "r") as f:
        data = json.load(f)
    # print(data)
    i = []
    for k in data:
        # print(k)
        i.append(f"${k}")
    # print(i)
    i = str(i)
    i = i.replace("'", "")
    i = i.replace(",", "")
    i = i.replace("]", "")
    i = i.replace("[", "")
    # print(i)
    html = html.replace('class="input">X', f'class="input">{i}')
    for k, v in data.items():
        data = f'<div class="{v}">{k}: {v}</div>'
        html = re.sub(f"\${k}", data, html)
    print(re.sub(f"\${k}", data, html))
    template.close()

    index = open("website/index.html", "w")
    index.write(html)
    index.close()


def delete(host):
    """
    deletes the host from the json file
    """
    with open("bestand.json", "r") as f:
        file = json.load(f)
    # print(file)
    try:
        del file[host]
    except:
        print("file does not exit")
    with open("bestand.json", "w") as f:
        json.dump(file, f, indent=2)


def show():
    """
    Shows all of the sites and there state
    """
    with open("bestand.json", "r") as f:
        data = json.load(f)
    for k, v in data.items():
        if v == "True":
            console.print(f"{k}: {v}", style="bold green")
        if v == "False":
            console.print(f"{k}: {v}", style="bold red")


def pingAll():
    """Goes trought all of the sites in the json file and ping them"""
    with open("bestand.json", "r") as f:
        data = json.load(f)
    for k in data:
        ping(k)
