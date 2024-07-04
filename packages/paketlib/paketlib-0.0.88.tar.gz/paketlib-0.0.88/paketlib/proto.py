from . import pkcrypt
import hashlib
import socket
import base64
import zlib
import os

class ProtoCrypt:
    def __init__(self):
        self.temp = ''

    def keygen(self, claddr: str) -> bytes:
        x_seciondat = bytes([len(os.listdir('.'))])
        y_seciondat = os.getcwd().split('/')[-1][:4].encode()
        z_seciondat = pkcrypt.xor(claddr[:4].encode(), bytes([0xaf, 0xff, 0xfa]))

        claddrz = zlib.compress(claddr.encode())
        structsplt = bytes([0x14, 0xff, 0x88])

        t_list = [x_seciondat, y_seciondat, z_seciondat, claddrz]
        struct = [dat + structsplt if dat != t_list[-1] else dat for dat in t_list]
        return b''.join(struct)
        



class Server:
    def __init__(self) -> None:
        pass