import time

from bs4 import BeautifulSoup
import requests

print('Tell job you dont want to do: ')
unfamiliar_job = input('>')


def find_jobs():
    html_text = requests.get('https://www.olx.pl/praca/q-praca/?search%5Bfilter_enum_contract%5D%5B0%5D=zlecenie').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find('table', class_='fixed offers breakword offers--top redesigned')
    jobs_names = jobs.find_all('h3', class_='lheight22 margintop5')
    jobs_wages = jobs.find_all('div', class_='list-item__price')
    jobs_infos = jobs.find_all('h3', class_='lheight22 margintop5')

    for i in range(len(jobs_wages)):
        if unfamiliar_job.lower() not in jobs_names[i].text.strip().lower():
            with open(f'posts/{i}.txt', 'w') as f:
                f.write(f'Job name: {jobs_names[i].text.strip()}')
                f.write(f'\nWage: {jobs_wages[i].text.strip()}')
                f.write(f"\nMore info: {jobs_infos[i].a['href']}")  # alt + shift
            print(f'File saved')


if __name__ == '__main__':
    while True:
        time_wait = 10
        find_jobs()
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
