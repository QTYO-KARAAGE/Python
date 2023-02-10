import socket
import sys

if (len(sys.argv) <= 1):
    str = str.encode('hello')
else:
    str = str.encode(sys.argv[1])
    
ipaddr = '127.0.0.1'
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect((ipaddr, port))
    # サーバにメッセージを送る
    s.send(str)
    # ネットワークのバッファサイズは1024。
    # サーバからの文字列を取得する
    data = s.recv(1024)
print(data)