import requests
import json
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(filename, new_filename, from_lang, to_lang='ru'):

    text = []
    with open(filename, 'r', encoding='utf8') as file_open:
        for line in file_open:
            text.append(line)

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}'.format(to_lang)
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    translation = ''.join(json_['text'])

    with open(new_filename, "w", encoding='utf8') as datafile:
        datafile.writelines(translation)
        datafile.write(f'\n Переведено сервисом «Яндекс.Переводчик» <http://translate.yandex.ru>')
    return new_filename

if __name__ == '__main__':
    print(translate_it('ES.txt', 'translation_from_ES.txt', 'es'))