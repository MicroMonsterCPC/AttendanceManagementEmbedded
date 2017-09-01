from ReadPasori import ReadPasori 
from PostJson import PostJson
from PlaySound import PlaySound

if __name__ == '__main__':
  for i in xrange(5):
    print "Waiting..."
    idm = ReadPasori.read_idm()
    if (idm == ''):
      # ignore
      next
    print idm
    status = PostJson.create(idm)['status']
    print status
