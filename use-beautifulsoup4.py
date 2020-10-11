import requests
from bs4 import BeautifulSoup

url = 'https://dw.com'
try:
  response = requests.get(url)
  if response.status_code == 200:
    print(f'Success! Response = {response.status_code}')
    #print(f'Content \n {response.text}')
    soup = BeautifulSoup(response.text, features="html.parser")
    print(f'the result of the URL call {url}')
    print(f'Title: {soup.title.string}')
    print(f'{soup.get_text()}')
  else:
    print(f' wrong request{response.status_code}')
except Exception as e:
  print(f'There is an error {e}')
print('Program ended')