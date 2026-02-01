import socket  # lib para conexões
import threading  # lib para processamento simultâneo

#criando dicionário com portas -----------------------------------------------
portas_comuns = {
    20: "FTP Data – Transferência de arquivos",
    21: "FTP Control – Controle de transferência de arquivos",
    22: "SSH – Acesso remoto seguro",
    23: "Telnet – Acesso remoto (inseguro)",
    25: "SMTP – Envio de e-mails",
    53: "DNS – Resolução de nomes",
    67: "DHCP – Servidor (atribuição de IP)",
    68: "DHCP – Cliente",
    69: "TFTP – Transferência simples de arquivos",
    80: "HTTP – Serviço web",
    110: "POP3 – Recebimento de e-mails",
    119: "NNTP – Notícias (Usenet)",
    123: "NTP – Sincronização de horário",
    137: "NetBIOS – Serviço de nomes",
    138: "NetBIOS – Serviço de datagrama",
    139: "NetBIOS – Sessão",
    143: "IMAP – Recebimento de e-mails",
    161: "SNMP – Gerenciamento de rede",
    162: "SNMP – Trap",
    179: "BGP – Roteamento entre sistemas",
    389: "LDAP – Serviço de diretório",
    443: "HTTPS – Serviço web seguro",
    445: "SMB – Compartilhamento de arquivos (Windows)",
    465: "SMTPS – SMTP seguro",
    500: "ISAKMP – VPN (IPsec)",
    514: "Syslog – Logs do sistema",
    520: "RIP – Protocolo de roteamento",
    587: "SMTP – Envio de e-mails (TLS)",
    636: "LDAPS – LDAP seguro",
    989: "FTPS – FTP seguro (dados)",
    990: "FTPS – FTP seguro (controle)",
    993: "IMAPS – IMAP seguro",
    995: "POP3S – POP3 seguro",
    1433: "MSSQL – Banco de dados Microsoft",
    1521: "Oracle DB – Banco de dados",
    2049: "NFS – Sistema de arquivos de rede",
    2082: "cPanel – Administração web",
    2083: "cPanel – Administração web segura",
    2086: "WHM – Administração de servidor",
    2087: "WHM – Administração segura",
    2181: "Zookeeper – Coordenação distribuída",
    2375: "Docker – API não segura",
    2376: "Docker – API segura",
    2483: "Oracle DB – Serviço TCP",
    2484: "Oracle DB – Serviço TCPS",
    3000: "Aplicações web / Dev servers",
    3306: "MySQL – Banco de dados",
    3389: "RDP – Área de trabalho remota",
    3690: "Subversion – Controle de versão",
    4444: "Metasploit – Listener comum",
    5432: "PostgreSQL – Banco de dados",
    5601: "Kibana – Dashboard",
    5672: "AMQP – RabbitMQ",
    5900: "VNC – Acesso remoto gráfico",
    5985: "WinRM – Gerenciamento remoto",
    5986: "WinRM – Gerenciamento remoto seguro",
    6379: "Redis – Banco de dados em memória",
    6443: "Kubernetes API Server",
    6667: "IRC – Chat",
    7001: "WebLogic – Aplicação Java",
    7002: "WebLogic – Aplicação segura",
    8000: "HTTP Alternativo / Dev",
    8008: "HTTP Alternativo",
    8080: "HTTP Proxy / Alternativo",
    8443: "HTTPS Alternativo",
    9000: "Aplicações diversas / Dev",
    9042: "Cassandra – Banco de dados",
    9200: "Elasticsearch – API",
    9418: "Git – Controle de versão",
    27017: "MongoDB – Banco de dados"
}


# recebendo info -------------------------------
endereço = input("Digite o domínio ou IP para escanear: ") # receb endereço do usuário

porta_init = int(input("Porta inicial: "))# recebe porta inicial
porta_end = int(input("Porta final: "))# recebe porta final

print(f"\nEscaneando {endereço}...\n") # menssagem de trabalho
# ---------------------------------------------

# definindo função scan -------------------------
def scan(porta):
    try:# tratamento de erros 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# usa socket para sacanear porta
        s.settimeout(0.5)#define tempo maxímo para pular de porta
        result = s.connect_ex((endereço, porta))# recebe resultado do scan

        if result == 0: # se der certo devolver resultado do sacan
            
            servico = portas_comuns.get(porta, "Serviço desconhecido") # puxa descrição do dicionário
            
            print(f"[+] Porta {porta} ABERTA → {servico}") # imprime resultado na tela 


        s.close()# fecha scan
    except:# trata erro

        pass
# ---------------------------------------------

threads = []  #cria  lista de threads
# exxecutando scan___________________________________________
for porta in range(porta_init, porta_end): # laço for percorrendo por portas
   
    t = threading.Thread(target=scan, args=(porta,))# cria nova thread para execução paralela
   
    threads.append(t) #adiciona nova therad criada a lista
    
    t.start()#inicia execução da thread 

for t in threads: #percorre lista threads
    t.join() # faz o programa esperar
#-----------------------------------------------------------------------
print("\nScan finalizado.")# mensagem de termino

#feito por jgbarreiros
#https://github.com/jgbarreiros

import pyfiglet

assinatura = pyfiglet.figlet_format("@jgbarreiros")#prompzinho de assinatura
print(assinatura)
