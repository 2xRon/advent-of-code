import os
import requests
import sys



def inp(cookie: str, day: int, year: int = 2018):
    COOKIES = {'session' : cookie}
 
    path = os.path.join(os.path.dirname(__file__), 'inputs', f'{day:02d}.input')
    
    if os.path.exists(path):
        return open(path).read()

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    data = requests.get(url, cookies=COOKIES)

    if data.status_code != 200:
        raise Exception(data.text)
    
    with open(path,'w') as f:
        f.write(data.text)

    return data.text

if __name__ == '__main__':
    # fug u jdartz
    session_cookie = open('COOKIE.secret','r').read().strip()
    if len(sys.argv) == 2:
       inp(session_cookie, int(sys.argv[1]))
    elif len(sys.argv) == 3:
       inp(int(session_cookie, sys.argv[1]), int(sys.argv[2]))

