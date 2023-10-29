import socket
import threading

# Configurações do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432  # Porta utilizada pelo servidor

# Função para enviar mensagens
def send_message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message = input("Digite uma mensagem para o servidor: ")
            s.sendall(message.encode())

# Função para receber respostas do servidor
def receive_response():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)
            print('Resposta recebida do servidor:', data.decode())

# Threads para enviar e receber mensagens
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_response)

# Iniciar as threads
send_thread.start()
receive_thread.start()