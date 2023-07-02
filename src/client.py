"""
TFTPy - This module implements an interactive and command line TFTP 
client.
    
This client accepts the following options:
    $ python3 client.py (get|put) [-p serv_port] server source_file [dest_file] 
    $ python3 client.py [-p serv_port] server

(C) João Galamba && Tiago Domingos, 2023
"""

import sys;

def main():
    while True:
        print("TFTPy - Cliente de TFTP")
        print("Receber ficheiro - get ficheiro_remoto [ficheiro_local]")
        # get ficheiro_remoto [ficheiro_local]
        print("Enviar ficheiro - put ficheiro_local [ficheiro_remoto]")
        # put ficheiro_local [ficheiro_remoto]
        print("Pretende Sair do TFTP? Insira quit...")
        # quit
        print("Quer Ajuda? Help ou ?")
        # help

        opcao = input("Opção > ")

        if opcao.upper() in ('GET', 'OBTER'):
            pass

        elif opcao.upper() in ('PUT', 'ENVIAR'):
            pass

        elif opcao.upper() in ('QUIT', 'SAIR'):
            print("Exiting TFTP client.")
            print("Goodbye!")
            sys.exit(0);
        
        elif opcao.upper() in ('HELP', 'AJUDA', '?'):
            ajuda()
        
        else:
            print(f"Opção {opcao} inválida")
#:

def ajuda():
    print("Commands:")
    print("  get remote_file [local_file] - get a file from server and save it as local_file")
    print("  get remote_file [local_file] - send a file to server and store it as remote_file")
    print("  dir                          - obtain a listing of remote files (not implementable)")
    print("  quit                         - exit TFTP client")

if __name__ == '__main__':
    main()
#:
