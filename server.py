import socket, threading
import speech_recognition as sr


clients = []

host = socket.gethostbyname(socket.gethostname())
port = 9090

sock = socket.socket()
sock.bind((host, port))


sock.listen(6)

def recode_volume():
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
       
        print(r.recognize_google(audio, language='ru-RU'))
        return r.recognize_google(audio, language='ru-RU')



def send_data():
    while True:
        for client in clients:
            client.send(f"{recode_volume()}".encode('utf-8'))

def add_new_clients():
    while True:
        conn, addr = sock.accept()
        print(f"connecnted {addr}")
        clients.append(conn)

send = threading.Thread(target=send_data)
send.start()

add = threading.Thread(target=add_new_clients)
add.start() 