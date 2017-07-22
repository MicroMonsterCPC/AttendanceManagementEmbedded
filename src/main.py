import binascii
import nfc
import json
import urllib2
import datetime
import config
import wave
import pyaudio

def play_sound(file):
  chunk = 1024
  
  wf = wave.open(file, 'r')
  p = pyaudio.PyAudio()

  stream = p.open(
    format = p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True)

  data = wf.readframes(chunk)

  while (data != ''):
    stream.write(data)
    data = wf.readframes(chunk)

  stream.close()
  p.terminate()

def play_enter():
  play_sound('../sound/enter.wav')

def play_left():
  play_sound('../sound/left.wav')

def play_touch():
  play_sound('../sound/touch.wav')

def play_cancel():
  play_sound('../sound/cancel.wav')

def play_error():
  play_sound('../sound/error.wav')

def post_data(url, obj):
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

def create_record(idm):
  url = config.settings['url'] + '/protect/attendances/create'
  obj = { 'idm': idm, 'datetime': str(datetime.datetime.today()) }
  return post_data(url, obj)

def destroy_record(idm):
  url = config.settings['url'] = '/protect/attendances/cancel'
  obj = { 'idm': idm }
  return post_data(url, obj)

def on_connect(tags):
  print 'Touch'
  play_touch()
  try:
    idm = binascii.hexlify(tags.idm)
    print idm
  except Exception:
    print 'Not supported IC'
    return False
  status = create_record(idm)['status']
  print status
  if (status == 'enter'):
    play_enter()
  elif (status == 'left'):
    play_left()
  else:
    play_error()

  return True 



for i in xrange(5):
  print 'Waiting'
  clf = nfc.ContactlessFrontend('usb')
  try: 
    clf.connect(rdwr={'on-connect': on_connect})
  #except Exception:
  #  print 'Unknown Error'
  #  next
  finally:
    clf.close()
  print 'Release'
