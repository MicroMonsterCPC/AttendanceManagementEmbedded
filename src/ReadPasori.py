import binascii
import nfc

class ReadPasori(object):
  @staticmethod
  def read_idm():
    clf = nfc.ContactlessFrontend('usb')
    try:
      idm = binascii.hexlify(clf.connect(rdwr={'on-connect': lambda tag: False}).idm)
    except Exception:
      idm = ''
    finally:
      clf.close()
    return idm

