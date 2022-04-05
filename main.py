import requests
from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
word = (input('Enter a word: '))
data = get(BASE_URL + word).json()

meanings = data[0]['meanings'][0]['definitions']

i = 0
print("--------MEANINGS-----------")
for meaning in meanings:
    i += 1
    print(f"{i}.{meaning['definition']}")

# tlumaczenie na jezyk polski:
html_text = requests.get('https://www.diki.pl/slownik-angielskiego?q=' + word).text
soup = BeautifulSoup(html_text, 'lxml')

native_lang_meanings = soup.find('ol', class_="foreignToNativeMeanings")

sjp_html = requests.get('https://sjp.pl/' + native_lang_meanings.span.a.text).text
soup_sjp = BeautifulSoup(sjp_html, 'lxml')
polish_word_meanings = soup_sjp.find('p', style="margin: .5em 0; font: medium/1.4 sans-serif; max-width: 34em; ")


def print_polish_meanings():
    for polish_meaning in polish_word_meanings.text.split(';'):
        print(polish_meaning)


print(f'\nMeaning of the word "{word}" in polish: {native_lang_meanings.span.a.text}')
print(f'\nAccording to sjp (polish dictonary) it has meanings:')
print_polish_meanings()
