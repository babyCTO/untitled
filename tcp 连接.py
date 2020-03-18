import socket,threading
#创建连接
sock_sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地IP地址
host=socket.getsockname()
#设置端口号
port=1236
#绑定端口
sock_sk.bind(host,port)
#设置最大连接数
sock_sk.listen(5)
#建立连接
socket.connnect(host,port)