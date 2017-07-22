import json
import urllib2
import time
import config

class PostJson(object):
  @staticmethod 
  def __post(url, obj):
    username = config.settings['user']
    password = config.settings['pass']
    headers = {
      'Content-Type': 'application/json',
      'authorization': 'Basic ' + (username + ':' + password).encode('base64')[:-1]
    }
    
    data = json.dumps(obj).encode('utf-8')

    req = urllib2.Request(url, data=data, headers=headers)
    res = urllib2.urlopen(req)

    return json.loads(res.read().decode('utf-8'))

  @staticmethod
  def create(idm):
    url = config.settings['url'] + '/protect/attendances/create'
    obj = { 'idm': idm, 'datetime': time.time() }
    return PostJson.__post(url, obj)

  @staticmethod
  def cancel(idm):
    url = config.settings['url'] + '/protect/attendances/cancel'
    obj = { 'idm': idm }
    return PostJson.__post(url, obj) 

