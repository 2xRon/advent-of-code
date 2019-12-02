#!/usr/bin/python

import os
import requests
import sys
import re


def inp(cookie: str, day: int, year: int = 2019):
    COOKIES = {"session": cookie}

    path = os.path.join(os.path.dirname(__file__), "inputs", f"{day:02d}.input")

    if os.path.exists(path):
        return open(path).read()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    data = requests.get(url, cookies=COOKIES)

    if data.status_code != 200:
        raise Exception(data.text)

    with open(path, "w") as f:
        f.write(data.text)

    return data.text


def prep_file(day: int, year: int = 2019):
    url = f"https://adventofcode.com/{year}/day/{day}"
    data = requests.get(url)

    if data.status_code != 200:
        raise Exception(data.text)
    title = re.search(r"--- Day \d+: (.+) ---", data.text, re.DOTALL).group(1)
    filename = f"{day:02d}" + "_" + title.replace(" ", "_").lower() + ".py"
    path = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(path):
        print(f"Day {day} file already exists.")
        return
    with open(path, "w") as out_file:
        header = [
            '"""\n',
            f"AOC {year}\n",
            f"Day {day}: {title}\n",
            "Solution by 2xRon\n",
            '"""',
        ]
        for l in header:
            out_file.write(l)


if __name__ == "__main__":
    # fug u jdartz
    session_cookie = open("COOKIE.secret", "r").read().strip()
    if len(sys.argv) == 2:
        inp(session_cookie, int(sys.argv[1]))
        prep_file(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        inp(int(session_cookie, sys.argv[1]), int(sys.argv[2]))
        prep_file(int(sys.argv[1]), int(sys.argv[2]))
