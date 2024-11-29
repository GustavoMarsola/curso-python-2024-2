# Defina qual foi o lucro semanal do hotel
# Considere o valor da diária em R$ 142, 00
# Considere R$ 50,00 como custos de manutenção por diária de um hóspede

DIARIA_BRUTA = 142
CUSTOS_MANUTENCAO = 40
DIARIA_LIQUIDA = DIARIA_BRUTA - CUSTOS_MANUTENCAO
print('O valor líquido da diária é de: R$',DIARIA_LIQUIDA)

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

lucros_clientes = []

# 1 - Loopar sobre itens da lista

for i in hospedagens:
    print("Este é o item atual da lista, e contém os dados de hospedagem", i)
    # 2 - Em cada item, nos interessa saber sobre a quantidade de dias hospedado
    dias_hospedagem = i.get('dias_hospedagem')
    print("Quantidade de dias que que o cliente ficou hospedado: ", dias_hospedagem)
    # 3 - Multiplicar pelo valor líquido da diária
    lucro_cliente = dias_hospedagem * DIARIA_LIQUIDA
    print("O lucro diário em cima deste cliente foi de R$",lucro_cliente)
    # 4 - Armazenar este valor em uma estrutura de dados 
    lucros_clientes.append(lucro_cliente)

lucro_total = sum(lucros_clientes)

print('O lucro semanal do seu hotel foi de R$', lucro_total)

lucros_cliente = [x.get('dias_hospedagem') * DIARIA_LIQUIDA for x in hospedagens]
lucro_total = sum(lucros_clientes)
print('O lucro semanal do seu hotel foi de R$', lucro_total)

# Exercícios extra

# Determine qual foi o cliente que menos gerou lucro



