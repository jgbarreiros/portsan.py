🔍 Port Scanner em Python (Multithread)

Um scanner de portas em Python, usando sockets e multithreading, capaz de identificar portas abertas em um domínio ou endereço IP e exibir o serviço mais comum associado a cada porta.

🚀 Funcionalidades

Escaneia um intervalo de portas definido pelo usuário

Usa multithreading para maior velocidade

Identifica serviços comuns associados às portas abertas

Suporte a IP ou domínio

Timeout configurado para evitar travamentos

🛠️ Tecnologias Utilizadas

Python 3

socket (conexões de rede)

threading (execução paralela)

🧠 Como funciona

O programa cria uma thread para cada porta

Cada thread tenta se conectar à porta usando socket

Se a conexão for bem-sucedida, a porta é considerada aberta

O serviço é identificado através de um dicionário de portas comuns

⚠️ Aviso Legal

Este projeto é apenas para fins educacionais.
Utilize somente em redes e sistemas que você tem permissão para testar.

O uso indevido pode ser ilegal.

📄 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar.

🔍 Python Port Scanner (Multithread)

A Python-based port scanner using sockets and multithreading, capable of identifying open ports on a domain or IP address and displaying the most common service associated with each port.

🚀 Features

Scans a user-defined port range

Uses multithreading for higher scanning speed

Identifies common services associated with open ports

Supports IP address or domain name

Configurable timeout to prevent hanging

🛠️ Technologies Used

Python 3

socket (network connections)

threading (parallel execution)

🧠 How It Works

The program creates one thread per port

Each thread attempts to connect to the port using socket

If the connection is successful, the port is considered open

The service is identified using a dictionary of common ports

⚠️ Legal Disclaimer

This project is for educational purposes only.
Use only on networks and systems you are authorized to test.

Improper use may be illegal.

📄 License

This project is licensed under the MIT License.
