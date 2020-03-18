import socket,threading

#创建发送连接socke
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定本地IP
host=s.bind(('',4396))
def st():
    while True:
    #发送的信息
        data=str(input("<<:"))
    #创建发送连接
        s.sendto(data.encode("utf-8"),('192.168.0.107',1238))
        continue


def js():
    while True:
        #接收数据
        data1,addr=s.recvfrom(1024)
        #显示发送数据
        print(data1.decode("utf-8"),addr)
#建立多线程连接
tk1=threading.Thread(target=st)
tk2=threading.Thread(target=js)
tk1.start()
tk2.start()
tk1.join()#建立阻塞等待坏境
tk2.join()#建立阻塞等待坏境

#关闭连接
s.close()
