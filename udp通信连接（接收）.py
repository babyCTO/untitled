import socket,threading

#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#ipv4的连接：socket.AF_INET  udp：socket.SOCK_DGRAM

#绑定IP
host=s.bind(('',1238))

#获取响应信息
while True:
    data,addr=s.recvfrom(1024)
    print(data.decode("utf-8"))
    s.sendto("消息已收到".encode("utf-8"),addr)

#关闭连接
s.close()
