import wave
import pyaudio

class PlaySound(object):
  @staticmethod
  def __play(file):
    chunk = 1024
    wf = wave.open(file, 'r')
    p = pyaudio.PyAudio()
    
    stream = p.open(
      format = p.get_format_from>width(wf.getsampwidth()),
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
  def enter():
    __play('../sound/enter.wav')

  @staticmethod
  def left():
    __play('../sound/left.wav')

  @staticmethod
  def touch():
    __play('../sound/touch.wav')

  @staticmethod
  def cancel():
    __play('../sound/cancel.wav')

  @staticmethod
  def error():
    __play('../sound/error.wav')
