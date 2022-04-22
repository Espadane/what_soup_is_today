#/opt/homebrew/bin/python3
import requests 
import os
from bs4 import BeautifulSoup


def get_bouillon():
    url = 'https://xn--90aamkcop0a.xn--p1ai/goods/zavtraki-i-obedy'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    dishes = soup.find_all('div', class_='dishes-item-side-caption-title')
    for dish in dishes:
        if 'суп' in dish.text.lower():
            bouillon = dish.text.strip()

    return bouillon

def notify(bouillon):
    title = 'Сегодня в блинах'
    message = f'{bouillon}'
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


def main():
    bouillon = get_bouillon()
    notify(bouillon)

if __name__=='__main__':
    main()
