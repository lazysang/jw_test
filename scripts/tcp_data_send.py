import socket
import time
import random

def send_syslog_tcp(url,port):
    '''发送syslog日志'''
    if "//" in url:
        host = url.split("//")[1]
    else:
        host = url
    print(host)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    data = "<30>Oct 9 22:33:20 220.181.38.148 auditd[1787]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.\n"
    s.send(data.encode("raw-unicode-escape"))
    s.close()


if __name__ == "__main__":
    for i in range(1):
        print(i)
        send_syslog_tcp(url = "https://10.168.1.137", port="514")
        time.sleep(random.randint(1, 10)*0.1)
    # url = "https://10.168.1.137"
    # host = url.split("//")[1]
    # print(host)
    pass
