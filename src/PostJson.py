import json
import urllib2
import time
import os

class PostJson(object):
  @staticmethod
  def create(idm):
   url = os.environ.get('AttendanceManagementUrl') + '/attendances/create'
   obj = { 'idm': idm, 'datetime': time.time() }
   return __post(url, obj)

  @staticmethod
  def cancel(idm):
    url = os.environ.get('AttendanceManagementUrl') + '/attendances/cancel'
    obj = { 'idm': idm }
    return __post(url, obj) 
   
  @staticmethod
  def __post(url, obj):
    username = os.environ.get('AttendanceManagementBasicUsername')
    password = os.environ.get('AttendanceManagementBasicPassword')
    headers = {
      'Content-Type': 'application/json',
      'authorization': 'Basic ' + (username + ':' + password).encode('base64')[:-1]
    }
    
    data = json.dumps(obj).encode('utf-8')

    req = urllib2.Request(url, data=data, headers=headers)
    res = urllib2.urlopen(req)

    return json.loads(res.read().decode('utf-8'))

