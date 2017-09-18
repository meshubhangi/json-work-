import urllib.parse
import requests

main_api ='https://opentdb.com/api.php?'
amount = '10'
category= '15'
difficulty= 'easy'
types= 'multiple'
url = main_api + urllib.parse.urlencode({'amount': amount})
print(url)
json_data = requests.get(url).json()
print(json_data)
