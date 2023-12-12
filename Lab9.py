import tkinter as tk
import socket
import requests

def send_message_socket(ip_address, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        sock.connect((ip_address, port))

        sock.sendall(message.encode())

    finally:

        sock.close()

def send_message_http(ip_address, message):
    url = f'http://{ip_address}/send'
    payload = {'message': message}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print('Сообщение успешно отправлено')
    else:
        print('Ошибка при отправке сообщения')

def send_message():
    message = entry.get()
    ip_address = '192.168.0.100'  # Здесь ip пользователя
    port = 5500  #Порт пользователя


    send_message_socket(ip_address, port, message)


    send_message_http(ip_address, message)

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Мессенджер")
messages_text = tk.Text(root)
messages_text.pack()
entry = tk.Entry(root)
entry.pack()
send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()

root.mainloop()

#Работоспособность проверить не получилось, но в теории должно работать :)
#Часть кода мне  написал gpt