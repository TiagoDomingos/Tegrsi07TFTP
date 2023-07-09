"""
TFTPy - This module implements an interactive and command line TFTP 
client.
    
This client accepts the following options:
    $ python3 client.py (get|put) [-p serv_port] server source_file [dest_file] 
    $ python3 client.py [-p serv_port] server

(C) João Galamba && Tiago Domingos, 2023
"""
# import docopt
import sys
from tftp import *

def main():
        if len(sys.argv) < 2:
            print("Comando inválido. Use 'get', 'put', ou 'tftf'.")
            sys.exit(1)

        comando = sys.argv[1]

        if comando == 'get':
            if len(sys.argv) < 4:
                print("Usage: python3 client.py get [-p serv_port] server source_file [dest_file]")
                sys.exit(1)

            server = sys.argv[2]
            source_file = sys.argv[3]
            dest_file = sys.argv[4] if len(sys.argv) >= 5 else None
            serv_port = int(sys.argv[3][3:]) if len(sys.argv) >= 5 and sys.argv[3].startswith('-p') else 69
            server_addr = (server, serv_port)

            try:
                get_file(server_addr, source_file, dest_file)
            except NetworkError as e:
                print(f"Error reaching the server '{server}' ({e}).")
            except ProtocolError as e:
                print(f"Protocol error: {e}")

        elif comando == 'put':
            if len(sys.argv) < 4:
                print("Usage: python3 client.py put [-p serv_port] server source_file [dest_file]")
                sys.exit(1)

            server = sys.argv[2]
            source_file = sys.argv[3]
            dest_file = sys.argv[4] if len(sys.argv) >= 5 else None
            serv_port = int(sys.argv[3][3:]) if len(sys.argv) >= 5 and sys.argv[3].startswith('-p') else 69
            server_addr = (server, serv_port)

            try:
                put_file(server, source_file, dest_file)
            except NetworkError as e:
                print(f"Error reaching the server '{server}' ({e}).")
            except ProtocolError as e:
                print(f"Protocol error: {e}")

        elif comando == 'tftp':
            while True:
                print("TFTPy - Cliente de TFTP")
                opcao = input('TFTP > ')
                if opcao in ('get'):
                    print("Receber ficheiro - get ficheiro_remoto [ficheiro_local]")
                    # get ficheiro_remoto [ficheiro_local]
                elif opcao in ('put'):
                    print("Enviar ficheiro - put ficheiro_local [ficheiro_remoto]")
                    # put ficheiro_local [ficheiro_remoto]
                elif opcao in ('help', '?'):
                    ajuda()
                elif opcao in 'quit':
                    print("Exiting TFTP client.")
                    print("Goodbye!")
                    sys.exit(0);
                else:
                    print(f"Opção {opcao} inválida")
        
        #elif opcao.upper() in ('HELP', 'AJUDA', '?'):
        #    ajuda()
        
        else:
            print(f"Opção {comando} inválida")
        #    print(ajuda())
#:

def ajuda():
    print("Commands:")
    print("  get remote_file [local_file] - get a file from server and save it as local_file")
    print("  get remote_file [local_file] - send a file to server and store it as remote_file")
    print("  dir                          - obtain a listing of remote files (not implementable)")
    print("  quit                         - exit TFTP client")

if __name__ == '__main__':
    #arguments = docopt(__doc__, version='TFTPy Python - 1')
    #print(arguments)
    main()
    
#:
