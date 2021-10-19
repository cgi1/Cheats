"""
Trivial: Creates one file per day in cron
@author: Christoph Giese
"""

import os, datetime, requests

BASE_DIR = os.getcwd()
BASE_DIR = '/var/www/html/daily/'

if not os.path.exists:
    os.makedirs(BASE_DIR)
    print(f"Created {BASE_DIR}")

if __name__ == '__main__':

    now = datetime.datetime.now().strftime('%Y-%m-%d')
    fstr = f"{now}.txt"
    fpath = os.path.join(BASE_DIR, fstr)

    # Fun part
    try:
        r = requests.get(url='https://quotes.rest/qod?language=en')
        quote_of_the_day = r.json()['contents']['quotes'][0]['quote']
        quote_of_the_day += f"\n     Author {r.json()['contents']['quotes'][0]['author']}"
    except:
        quote_of_the_day = 'No quote of today.'

    content = f'Today is {now}. \n\n{quote_of_the_day}'
    with open(fpath, 'w') as fout:
        fout.writelines(content)

    print(f"Wrote {fpath}: {content}")
