from ReadPasori import ReadPasori 
from PostJson import PostJson
from PlaySound import PlaySound

if __name__ == '__main__':
  print "Waiting..."
  idm = ReadPasori.read_idm()
  print idm
  status = PostJson.create(idm)['status']
  print status
