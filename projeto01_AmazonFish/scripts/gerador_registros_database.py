'''
// Gerador de Registros Aleatórios para o CSV
# Este script gera registros aleatórios para um arquivo CSV existente.
# Ele lê os dados existentes do arquivo, seleciona aleatoriamente produtos, categorias, condições climáticas e regiões, e cria novos registros com base nessas informações.
# O arquivo CSV deve ter um cabeçalho e os dados devem estar no formato correto.
# O script adiciona novos registros ao final do arquivo CSV existente.

// O arquivo CSV deve estar no seguinte formato:
# Data,Produto,Categoria,Preço Unitário,Quantidade Vendida,Condição Climática,Temperatura,Evento de Pesca,Região de Venda,Tempo de Navegação
# O script gera registros aleatórios entre 1º de abril de 2025 e 1º de maio de 2025.
# O script utiliza as bibliotecas csv, random, datetime e timedelta para manipulação de dados.
# Autor: [Paulo Roberto L. de F. Junior]
# Data: [20/04/2025]

# Certifique-se de que o arquivo CSV existe e está no formato correto antes de executar o script.
# O script pode ser executado em qualquer ambiente Python com as bibliotecas necessárias instaladas.
# Para executar o script, basta chamar a função adicionar_registros com o nome do arquivo CSV e o número de registros desejados.'''

# Importando bibliotecas necessárias
import csv
import random
from datetime import datetime, timedelta

# Função para gerar uma data aleatória entre duas datas
# A função gera uma data aleatória entre duas datas fornecidas como parâmetros.
def gerar_data_aleatoria(start_date, end_date):
    """Gera uma data aleatória entre duas datas."""
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime('%Y-%m-%d')

# Função para gerar um registro aleatório
# A função gera um registro aleatório com base em listas de produtos, categorias, condições climáticas e regiões.
# Ela seleciona aleatoriamente um produto, categoria, condição climática e região, e gera valores aleatórios para preço unitário, quantidade vendida, temperatura e tempo de navegação.
def gerar_registro_aleatorio(produtos, categorias, condicoes_climaticas, regioes):
    """Gera um registro aleatório com base nos dados fornecidos."""
    produto = random.choice(produtos)
    categoria = random.choice(categorias)
    preco_unitario = round(random.uniform(20, 950), 2)
    quantidade_vendida = random.randint(2, 45)
    condicao_climatica = random.choice(condicoes_climaticas)
    temperatura = random.randint(10, 35)
    evento_pesca = random.choice(['Sim', 'Não'])
    regiao_venda = random.choice(regioes)
    tempo_navegacao = random.randint(60, 350)
    
    return [
        gerar_data_aleatoria(datetime(2025, 4, 1), datetime(2025, 5, 1)),
        produto,
        categoria,
        str(preco_unitario),
        str(quantidade_vendida),
        condicao_climatica,
        str(temperatura),
        evento_pesca,
        regiao_venda,
        str(tempo_navegacao)
    ]

# Função para ler os dados existentes do arquivo CSV
# A função lê os dados existentes do arquivo CSV e armazena os produtos, categorias, condições climáticas e regiões em conjuntos.
def ler_dados_existentes(nome_arquivo):
    """Lê os dados existentes do arquivo CSV."""
    produtos = set()
    categorias = set()
    condicoes_climaticas = set()
    regioes = set()
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)  # Ignora o cabeçalho
        for linha in leitor_csv:
            produtos.add(linha[1])
            categorias.add(linha[2])
            condicoes_climaticas.add(linha[5])
            regioes.add(linha[8])
            
    return list(produtos), list(categorias), list(condicoes_climaticas), list(regioes)

# Função para adicionar novos registros ao arquivo CSV
# A função adiciona novos registros aleatórios ao arquivo CSV existente.
# Ela lê os dados existentes do arquivo, gera novos registros aleatórios e os adiciona ao final do arquivo.
def adicionar_registros(nome_arquivo, num_registros):
    """Adiciona novos registros aleatórios ao arquivo CSV."""
    produtos, categorias, condicoes_climaticas, regioes = ler_dados_existentes(nome_arquivo)
    
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for _ in range(num_registros):
            novo_registro = gerar_registro_aleatorio(produtos, categorias, condicoes_climaticas, regioes)
            escritor_csv.writerow(novo_registro)

# Nome do arquivo CSV
nome_arquivo = 'd:/GitHub Respositorios/microsoft-certification-challenge_DP100/database/amazonfish.csv'

# Número de registros a serem adicionados
num_registros = 50

# Adiciona os registros ao arquivo
adicionar_registros(nome_arquivo, num_registros)

print(f"{num_registros} registros aleatórios foram adicionados a '{nome_arquivo}'.")