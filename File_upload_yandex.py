import requests

GET_URL_FOR_UPLOAD = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {'path':'/translation_from_FR.txt', 'overwrite': 'true'} # менять название файла
TOKEN = 'OAuth AgAAAAAJ4N4vAADLW3292wczp03BmpZOwojK6Q8'
headers = {'Accept': 'application/json', 'Authorization' : TOKEN}

file_path = 'C:/Нетология/TXT/translation_from_FR.txt' # менять название файла

response = requests.get(GET_URL_FOR_UPLOAD, params=params, headers=headers)
print(response.text)

put_url = response.json().get('href')
print(put_url)

files = {'file': open(file_path, 'rb')}
response = requests.put(put_url, files=files)
print(response)
