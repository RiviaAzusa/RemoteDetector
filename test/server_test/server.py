import socket
from PIL import Image
from io import BytesIO
import re

def main():
    server = socket.socket()
    server.bind(('',11452))
    server.listen(2)
    conn,addr = server.accept()
    # data:bytes = b''
    data = conn.recv(630324)
    wdnmd_b = b'wdnmd'
    print(bool(re.search(wdnmd_b,data)))
    print(data[-5:])
    print(data[-5:].decode(encoding='utf-8'))
    while True:
        data_sub = conn.recv(1024)
        ans = re.search(b'wdnmd',data_sub)
        if bool(ans):
            print('okay')
            data+=data_sub[:ans.span()[0]]
            break
        else:
            data+=data_sub

    # data 
    print(len(data))
    image = Image.open(BytesIO(data))
    image.show()

    
main()