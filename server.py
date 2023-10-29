import socket
import random
import time

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432  # Porta utilizada pelo servidor

# Inicialização do socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Servidor escutando em {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            data = conn.recv(1024)
            if not data:
                break
            delay = random.uniform(0.1, 1.0)  # Delay aleatório
            time.sleep(delay)
            conn.sendall(b'Resposta do servidor: Recebido - ' + data)