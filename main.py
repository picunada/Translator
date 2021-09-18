import requests
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0'

lang = input(
    "Type \"en\" if you want to translate from French into English, or \"fr\" if you want to translate from English into French:\n")

word = input("Type the word you want to translate:\n")

if lang == 'en':
    print(f"You chose English as the language to translate \"{word}\"")
    language_1 = 'french'
    language_2 = 'english'
else:
    print(f"You chose French as the language to translate \"{word}\"")
    language_1 = 'english'
    language_2 = 'french'

url = f'https://context.reverso.net/translation/{language_1}-{language_2}/{word}'

r = requests.get(url, headers={'User-Agent': user_agent})
translations = []

if r.status_code == 200:
    print(f'{r.status_code} OK')
    print('Translations')
    soup = BeautifulSoup(r.content, 'html.parser')
    for i in soup.find('div', id="translations-content"):
        if "" not in i:
            translations.append(i.text.strip())

    translations[:0] = ['Translation']
    print(translations)
    en_sentences = []
    fr_sentences = []
    for word in soup.find_all('div', class_="src ltr"):
        en_sentences.append(word.text.strip())

    for word in soup.find_all('div', class_="trg ltr"):
        fr_sentences.append(word.text.strip())

    translation2 = [i for tup in zip(en_sentences, fr_sentences) for i in tup]
    translation2 = [line.rstrip() for line in translation2]
    print(translation2)
else:
    print(r.status_code)
