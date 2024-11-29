# Defina qual foi o lucro semanal do hotel
# Considere o valor da diária em R$ 142,00
# Considere R$ 40,00 como custos de manutenção por diária de um hóspede

DIARIA_BRUTA = 142
CUSTOS_MANUTENCAO = 40
# 1 - Reajustar o valor para diaria liquida, pois se trata de lucro 
diaria_liquida = DIARIA_BRUTA - CUSTOS_MANUTENCAO
print('O valor líquido da diária é de: R$', diaria_liquida)
print('\n')

hospedagens = (
    {
        "hospede": "Gustavo Marsola",
        "quarto": 204,
        "dias_hospedagem": 4
    },
    {
        "hospede": "Lucas Tracosa",
        "quarto": 307,
        "dias_hospedagem": 5
    },
    {
        "hospede": "Ronaldo Silva",
        "quarto": 106,
        "dias_hospedagem": 2
    },
    {
        "hospede": "Maria Oliveira",
        "quarto": 401,
        "dias_hospedagem": 4
    }
)

# 2 - Identificar a estrutura dos dados
# No caso, se trata de uma tupla que contém dicionários

# 3 - Descrever a solução em termos lógicos/matemáticos
# diaria_liquida * dias_hospedagem

# 4 - Comando for para percorrer os itens da tupla

for hospedagem in hospedagens:
    # print(hospedagem, type(hospedagem))
    cliente = hospedagem.get("hospede")
    # Acessando o item dias_hospedagem do dicionário
    qtd_diarias = hospedagem.get("dias_hospedagem")
    # Contabilizando o lucro do cliente
    lucro_cliente = qtd_diarias * diaria_liquida
    # print(f'O cliente {cliente} ficou hospedado por {qtd_diarias} dias')
    # print(f'Gerou um lucro de R$ {lucro_cliente}')
    # É possível formatar o valor para exibir uma msg em formato "humano"
    # print(f'Gerou um lucro de R$ {str(lucro_cliente).replace(".", ",")},00')
    # print('\n')

# 5 - Devemos somar os lucros de cada cliente

# 5.1 - Primeira alternativa é usar o recurso acumulativo

lucro_total = 0

for hospedagem in hospedagens:
    qtd_diarias = hospedagem.get("dias_hospedagem")
    lucro_cliente = qtd_diarias * diaria_liquida
    
    lucro_total += lucro_cliente
    # print(f'Parcial acumulativo: {lucro_total}')

# print('\n')
# print(f'O lucro total semanal do hotel foi de {lucro_total}')

# 5.2 - Podemos resolver com uma lista

lucro_total = []

for hospedagem in hospedagens:
    qtd_diarias = hospedagem.get("dias_hospedagem")
    lucro_cliente = qtd_diarias * diaria_liquida
    
    lucro_total.append(lucro_cliente)

lucro_total = sum(lucro_total)
print(f'O lucro total semanal do hotel foi de {lucro_total}')


