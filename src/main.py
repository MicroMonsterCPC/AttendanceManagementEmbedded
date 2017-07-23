import binascii
import nfc
import json
import urllib2
import datetime
import config
import wave
import pyaudio

idm = ''
touch_time = datetime.datetime.today()

class PlaySound(object):
  @staticmethod
  def __play_sound(file):
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
 
  @staticmethod 
  def play_enter():
    PlaySound.__play_sound('../sound/enter.wav')
  
  @staticmethod 
  def play_left():
    PlaySound.__play_sound('../sound/left.wav')
  
  @staticmethod 
  def play_touch():
    PlaySound.__play_sound('../sound/touch.wav')
  
  @staticmethod 
  def play_cancel():
    PlaySound.__play_sound('../sound/cancel.wav')
  
  @staticmethod 
  def play_error():
    PlaySound.__play_sound('../sound/error.wav')

class PostJson(object):
  @staticmethod
  def __post_data_with_basic(url, obj):
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
  def create_record(idm):
    url = config.settings['url'] + '/protect/attendances/create'
    obj = { 'idm': idm, 'datetime': str(datetime.datetime.today()) }
    return PostJson.__post_data_with_basic(url, obj)
  
  @staticmethod 
  def destroy_record(idm):
    url = config.settings['url'] + '/protect/attendances/cancel'
    obj = { 'idm': idm }
    return PostJson.__post_data_with_basic(url, obj)

class ReadPasori(object):
  idm = ''
  touch_time = datetime.datetime.today()
  
  @staticmethod 
  def on_connect(tags):
    print 'Touch'
    PlaySound.play_touch()
    ReadPasori.touch_time = datetime.datetime.today()
    ReadPasori.idm = binascii.hexlify(tags.idm)
    
    status = PostJson.create_record(ReadPasori.idm)['status']
    print status
    if (status == 'enter'):
      PlaySound.play_enter()
    elif (status == 'left'):
      PlaySound.play_left()
    else:
      PlaySound.play_error()
    
    return True 
  
  @staticmethod 
  def read():
    clf = nfc.ContactlessFrontend('usb')
    try:
      clf.connect(rdwr={'on-connect': ReadPasori.on_connect})
    #except:
    #  return False;
    finally:
      clf.close()
    return True


while (True):
  print 'Waiting'
  if (ReadPasori.read() == False):
    print 'Not Supported IC'
    next
  print 'Release'
  
  release_time = datetime.datetime.today()
  if ((release_time - ReadPasori.touch_time).seconds >= 3):
    if (ReadPasori.idm != ''):
      print ReadPasori.idm
      status = PostJson.destroy_record(ReadPasori.idm)['status']
      if (status == 'succeeded'):
        print 'Cancel Succeeded'
        PlaySound.play_cancel()
      else:
        print 'Cancel Failed'
        PlaySound.play_error()
  ReadPasori.idm = ''

