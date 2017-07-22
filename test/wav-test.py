import wave
import pyaudio

def play(file):
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

def enter():
  play('../sound/enter.wav')

def left():
  play('../sound/left.wav')

def touch():
  play('../sound/touch.wav')

def cancel():
  play('../sound/cancel.wav')

def error():
  play('../sound/error.wav')

enter()
