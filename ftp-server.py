from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/Users/AySanni", perm="Accompl!sh21")
authorizer.add_anonymous("/Users/AySanni/Desktop/Misc.", perm="Accompl!sh21")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1033), handler)
server.serve_forever()