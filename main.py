import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0'

languages = {
        '1': 'arabic',
        '2': 'german',
        '3': 'english',
        '4': 'spanish',
        '5': 'french',
        '6': 'hebrew',
        '7': 'japanese',
        '8': 'dutch',
        '9': 'polish',
        '10': 'portuguese',
        '11': 'romanian',
        '12': 'russian',
        '13': 'turkish'
    }

def output_words(array):
    x = 0
    for sentence in array:
        if x >= 5:
            print('\n')
            break
        print(f"{sentence}")
        x += 1


def output_sentence(array):
    x = 0
    y = 0
    for sentence in array:
        y += 1
        if x >= 10:
            print('\n')
            break
        print(f"{sentence}")
        if y % 2 == 0 and y != 0:
            print('\n')
        x += 1


def print_languages():
    for key in languages.keys():
        print(f"{key}. {languages[key].capitalize()}")


print(
    "Hello, you're welcome to the translator. Translator supports: \n")

print_languages()
lang = input("Type the number of your language: ")
lang_to_translate = input("Type the number of language you want to translate to: ")
word = input("Type the word you want to translate:\n")


print(f"You chose {languages[lang_to_translate].capitalize()} as the language to translate \"{word}\"")
language_1 = languages[lang]
language_2 = languages[lang_to_translate]


url = f'https://context.reverso.net/translation/{language_1}-{language_2}/{word}'

r = requests.get(url, headers={'User-Agent': user_agent})
translations = []

if r.status_code == 200:
    print(f'{r.status_code} OK')
    print(f'{language_2.capitalize()} Translations: ')
    soup = BeautifulSoup(r.content, 'html.parser')
    for i in soup.find('div', id="translations-content"):
        if "" not in i:
            translations.append(i.text.strip())

    # translations[:0] = ['Translation']
    output_words(translations)
    en_sentences = []
    fr_sentences = []
    for word in soup.find_all('div', class_="src ltr"):
        en_sentences.append(word.text.strip())

    for word in soup.find_all('div', class_="trg ltr"):
        fr_sentences.append(word.text.strip())

    translation2 = [i for tup in zip(en_sentences, fr_sentences) for i in tup]
    translation2 = [line.rstrip() for line in translation2]
    print(f"{language_2.capitalize()} Examples: ")
    output_sentence(translation2)
else:
    print(r.status_code)
