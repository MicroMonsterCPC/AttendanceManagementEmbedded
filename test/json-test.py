import json
import urllib2
from time import time

url = raw_input('Target URL: ')
method = 'POST'
username = raw_input('Username: ')
password = raw_input('Password: ')
headers = {
  'Content-Type': 'application/json',
  'authorization': 'Basic ' + (username + ':' + password).encode('base64')[:-1]
  }

obj = { 'idm': '1145148101919', 'datetime': time() }
data = json.dumps(obj).encode('utf-8')

req = urllib2.Request(url, data=data, headers=headers)
res = urllib2.urlopen(req)

print res.read().decode('utf-8')
