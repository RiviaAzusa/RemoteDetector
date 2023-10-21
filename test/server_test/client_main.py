import socket
from PIL import Image
from io import BytesIO
import re
def main():
    server = socket.socket()
    server.connect(('',11452))
    img = '/Users/azusa/research/project/smoke_detector/resources/images/1533577358_+00900.jpg'
    img = Image.open(img)
    img_bytes = BytesIO()
    img.save(img_bytes,format='JPEG')
    b = img_bytes.getvalue()
    print(len(b))
    # b += 'wdnmd'.encode(encoding='utf-8')
    server.send(b)
    print('sending over')

def test():
    m = 'kjdsjfaldfj'.encode()
    m_sub = 'wdnmd'.encode()
    print(m,m_sub)
    mm = m+m_sub
    print(mm)
    print(mm[:-5])

def test1():
    m = bytes('wdnmd'.encode())
    print(m)
    ans = re.search(b'wdnmd', m)
    print(bool(ans))
    print(ans)

def test2():
    img = '/Users/azusa/research/project/smoke_detector/resources/images/1533577358_+00900.jpg'
    img = Image.open(img)
    img_bytes = BytesIO()
    img.save(img_bytes,format='JPEG')
    b = img_bytes.getvalue()
    print(len(b))
    bp = b +b'wdnmd'
    ans = re.search(b'wdnmd',bp)
    # print(ans.span()[0])
    print(len(bp))
    b_ = bp[:ans.span()[0]]
    print(len(b_))
    print(len(b'wdnmd'))
    img_ = Image.open(BytesIO(b_))

    # img_ = Image.open(b_)
    img_.show()

main()
# test1()
# test2()