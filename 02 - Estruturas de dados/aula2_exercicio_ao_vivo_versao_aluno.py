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
