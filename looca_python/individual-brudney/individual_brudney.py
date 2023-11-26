import mysql.connector #biblioteca responsável pela conexão com o mysql
import time
from datetime import datetime
import psutil
import socket
import requests #Biblioteca responsável por conectar o SLACK com o pyhton
import speedtest
import re

# -----------------------------------------------------------------------------------------------------

print("Olá, bem vindo. O sistema da TEST foi iniciado!")

# -----------------------------------------------------------------------------------------------------

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0212',
    database='test'
)

# -----------------------------------------------------------------------------------------------------
st = speedtest.Speedtest()
cursor = connection.cursor()
net_before = psutil.net_io_counters()

#Criando a estrutura de repetição para que os valores dos componentes se atualizam
while True:
    #------------------------------------------------------------------------------------------------------

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    #------------------------------------------------------------------------------------------------------

    resposta = requests.get('https://httpbin.org/ip')

    # Converte a resposta para formato JSON
    dados_json = resposta.json()

    # Extrai o endereço IP público da resposta
    ip_publico = dados_json['origin']

    print(f"IP público: {ip_publico} ms")

    #-----------------------------------------------------------------------------------------------------


    # Medir a latência (ping)
    ping_result = st.get_best_server()
    ping_latency = ping_result["latency"]

    print(f"Latência da Internet: {ping_latency} ms")

    #-----------------------------------------------------------------------------------------------------


    dia = datetime.now()

    sql55 = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    values55 = (round(ping_latency, 2), dia.strftime('%Y-%m-%d %H:%M:%S'), 4, 1)

    sql66 = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    # values66 = (velocidade, dia.strftime('%Y-%m-%d %H:%M:%S'), 7, 1)

    #-----------------------------------------------------------------------------------------------------

    # # SQL para inserir na tabela detalhe
    sql2 = "INSERT INTO detalhe (IPV4, IPpublico, fkServidor) VALUES (%s, %s, %s)"
    values2 = (ip_address, ip_publico, 1)

    #-----------------------------------------------------------------------------------------------------

    sql22 = "INSERT INTO RegistrosRAW (dadosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    # values22 = (velocidade, dia.strftime('%Y-%m-%d %H:%M:%S'), 7, 1)

    sql222 = "INSERT INTO RegistrosRAW (dadosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    values222 = (round(ping_latency, 2), dia.strftime('%Y-%m-%d %H:%M:%S'), 4, 1)

    #-----------------------------------------------------------------------------------------------------

#Aqui, independente do valor e dos alertas os dados serão inseridos
    try:
        # Executa a inserção
        cursor.execute(sql2, values2)
        cursor.execute(sql222, values222)

        cursor.execute(sql55, values55)

        # Confirma as alterações no banco de dados
        connection.commit()
        print("Inserção de dados de REDE realizada com sucesso!")

    except mysql.connector.Error as err:
        print("Erro ao inserir nas tabelas Registros:", err)

    time.sleep(1)
