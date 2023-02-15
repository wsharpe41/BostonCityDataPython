# read json from url and print the data
import json
import urllib.request
import urllib.parse
import urllib.error

url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
# print type of data
print(type(data))
# convert data to json
js = json.loads(data)
# print type of js
print(type(js))
data = js["data"]
print(data[0])