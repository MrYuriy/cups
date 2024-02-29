import socket
import urequests
import ssl
import usocket as socket


def print_label(label_info):
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
    host = "printer_ip" 
    port = 9100   
    try:
        mysocket.connect((host, port))
        #print(len(label_info))
        for label in label_info:     
            mysocket.send(label.encode("utf-8"))
        mysocket.close () #closing connection
    except:
        pass
        #print("Error with the connection")

def get_label_code(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

    r = urequests.get(url, headers=headers)
    if r:
        return r.json()["label_code"]


