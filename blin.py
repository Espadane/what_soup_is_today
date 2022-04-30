#/opt/homebrew/bin/python3
import requests 
import os
from bs4 import BeautifulSoup


def get_bouillon():
    url = 'https://блинбери.рф/goods/zavtraki-i-obedy'
    r = requests.get(url)
    sup = []
    soup = BeautifulSoup(r.text, 'lxml')
    dishes = soup.find_all('div', class_='dishes-item-side-caption-title')
    for dish in dishes:
        if 'суп' in dish.text.lower():
            sup.append(dish.text.strip())
            
    return sup

def notify(bouillon):
    title = 'Сегодня в блинах'
    message = f'{bouillon}'
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


def main():
    bouillon = get_bouillon()
    if bouillon == []:
        bouillon = 'Или борщ или супа вообще нет'
    else:
        bouillon = bouillon[0]
    notify(bouillon)

if __name__=='__main__':
    main()
