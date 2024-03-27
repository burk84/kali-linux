import socket

print("""\n
                    

██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ 
██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                                                
                                                                                  
""") 

# Função para enviar solicitação HEAD
def send_head_request(site, porta):
    try:
        with socket.create_connection((site, porta), timeout=5) as conn:
            conn.sendall(b"HEAD / HTTP/1.1\r\nHost: " + site.encode() + b"\r\nConnection: close\r\n\r\n")
            response = conn.recv(4096).decode()
            print(f"\n🟢 Resposta da porta {porta}\n")
            print(response)
    except Exception as e:
        pass  # Não faz nada se a porta estiver fechada

if __name__ == "__main__":
    # Solicita ao usuário o nome do site
    site = input("\nDigite o nome do WebSite: ")

    # Verifica se o nome do site foi fornecido
    if not site:
        print("\nVocê não forneceu um nome de site válido. Saindo")
        exit(1)

    # Solicita ao usuário a entrada de portas
    porta_input = input("\nDigite as portas separadas por vírgula ou um intervalo de portas (exemplo:21,22,23,25  21-80 ou 80): ")

    # Verifica se a entrada é um intervalo ou uma lista de portas separadas por vírgula
    if '-' in porta_input:
        try:
            inicio, fim = map(int, porta_input.split('-'))
            if not 0 < inicio <= fim <= 65535:
                raise ValueError
            portas = range(inicio, fim + 1)
            print(f"\nEnviando solicitação 🟢 HEAD 🟢 para {site} nas portas: {inicio}-{fim}\n")
        except ValueError:
            print("\nIntervalo de portas inválido. Saindo")
            exit(1)
    else:
        portas = []
        try:
            for porta in map(int, porta_input.split(',')):
                if not 0 < porta <= 65535:
                    raise ValueError
                portas.append(porta)
            print(f"\nEnviando solicitação 🟢 HEAD 🟢 para {site} nas portas: {', '.join(map(str, portas))}\n")
        except ValueError:
            print("\nLista de portas inválida. Saindo")
            exit(1)

    # Verifica as portas e envia solicitações HEAD apenas para portas abertas
    for porta in portas:
        send_head_request(site, porta)

    input("\n🎯 Pressione Enter para sair 🎯 \n")
