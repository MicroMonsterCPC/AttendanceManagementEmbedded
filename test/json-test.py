import json
import urllib2
from time import time
from os import environ

print environ.get('AttendanceManagementTargetUrl')
url = environ.get('AttendanceManagementTargetUrl') + '/attendances/create'
method = 'POST'
username = environ.get('AttendanceManagementBasicUsername')
password = environ.get('AttendanceManagementBasicPassword')
headers = {
  'Content-Type': 'application/json',
  'authorization': 'Basic ' + (username + ':' + password).encode('base64')[:-1]
  }

obj = { 'idm': '1145148101919', 'datetime': time() }
data = json.dumps(obj).encode('utf-8')

req = urllib2.Request(url, data=data, headers=headers)
res = urllib2.urlopen(req)

print res.read().decode('utf-8')
