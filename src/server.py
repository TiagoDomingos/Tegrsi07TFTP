"""
Aqui é o módulo do servidor e faz a gestão do mesmo.

Data de entrega 14/07/2023

(C) Tiago Domingos, 2023
"""


from socketserver import BaseRequestHandler, ThreadingUDPServer
from socket import socket, AF_INET, SOCK_DGRAM
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        # Obter mensagem e um socket cliente
        msg = self.request[0]
        print('Got request', msg, 'from', self.client_address)
        resp = time.ctime()

        # Criar outro socket com um porto efémero para a resposta
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.sendto(resp.encode(), self.client_address)


if __name__ == '__main__':
    # Threading server permite servir múltiplos pedidos ao mesmo tempo
    ThreadingUDPServer.allow_reuse_address = True
    serv = ThreadingUDPServer(('localhost'), 20022), TimeHandler)
    print('Starting server...', serv)
    serv.serve_forever()
