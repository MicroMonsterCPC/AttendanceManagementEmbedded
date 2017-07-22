from ReadPasori import ReadPasori 
from PostJson import PostJson
if __name__ == '__main__':
  idm = ReadPasori.read_idm()
  print PostJson.create(idm)

