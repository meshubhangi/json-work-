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

#New codes with changes

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
#print(json_data)
json_response= json_data['response_code']
print('response code:',json_response)
print("enter the index")
i= int(input())
abc= json_data['results'][i]['category']
abc1= json_data['results'][i]['type']
abc2= json_data['results'][i]['difficulty']
abc3= json_data['results'][i]['question']
print(abc)
print(abc1)
print(abc2)
print(abc3)
