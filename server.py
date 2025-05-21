import socket

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor escutando em {PORT}...")
conn, addr = server.accept()
print(f"Cliente conectado: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        print("Cliente desconectado.")
        break
    print("Recebido:", data.decode())
    conn.sendall(b"Mensagem recebida!")

conn.close()
