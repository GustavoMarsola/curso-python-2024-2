# Exercício 1: Calculo do custo da estadia de um hóspede no hotel.

# Objetivo: O aluno deve usar variáveis, tipos numéricos e booleanos.

# Requisitos:

##<<<<<<< HEAD
usuario = 'Lucas Oliveira'
cantidad_diaria = int('3')
custo_diaria = 'R$ 127,00'
custo_diaria = custo_diaria.replace('R$ ', '').replace(',','.')
custo_diaria = float(custo_diaria)


custo_estadia = cantidad_diaria*custo_diaria
custo_estadia = str(custo_estadia).replace('.',',')
print('custo de la estadia estadia: R$', custo_estadia)



# O aluno deve perguntar ao usuário quantos dias ele ficará (número).
# Valor da diária é de R$ 127,00 (número) .
##=======
# O aluno deve perguntar ao usuário quantos dias ele ficará hospedado.
# Valor da diária é de R$ 127,00 .
#>>>>>>> dcd3e6159263b0f0f30e6268327e2c99854c06d9



# Exercício 2: Verifique se os dados do cliente estão corretos em relação ao seu registro no banco de dados

# Dados preenchidos pelo cliente

nome = 'Joao da silva souza'
cpf = '123456789-00'
incluso_cafe_da_manha = 0

# Dados do banco de dados
nome_db = 'JOAO DA SILVA SOUZA'
cpf_db = 12345678900
incluso_cafe_da_manha_db = False



conferir_nome = nome.upper()==nome_db.upper()
# o mais adequado para este caso seria a segunda solução comentada linha 43
cpf_db = str(cpf_db).replace('90','9-0')
#cpf_db = cpf_db.replace('-', '')
#cpf_db = int(cpf_db)

# para selecionar comand c (copiar) + Comand D (selecionar varias recorrencias) + comand v (colar)
conferir_cpf = cpf==cpf_db
conferir_cafe = bool(incluso_cafe_da_manha)==incluso_cafe_da_manha_db
print(conferir_nome)
print(conferir_cpf)
print(conferir_cafe)