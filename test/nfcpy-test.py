import binascii
import nfc

def on_connect(tag):
  print "Touched"
  try:
    print binascii.hexlify(tag.idm)
  except Exception:
    print "Error"
    return False
  return True

def read_id():
  print "Waiting"
  clf = nfc.ContactlessFrontend('usb')
  try:
    clf.connect(rdwr={'on-connect': on_connect})
  finally:
    clf.close()
  print "Release"

for i in xrange(5):
  read_id()
