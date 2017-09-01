import binascii
import nfc

class ReadPasori(object):
  def __init__():
    clf = nfc.ContactlessFrontend('usb')

  def on_connect():
    try:
      idm = binascii.hexlify(clf.connect(rdwr={'on-connect': lambda tag: False}).idm)
      clf.connect(rdwr={'on-release': lambda tag: False})
    except Exception:
      idm = ''
    finally:
      clf.close()
    return idm

