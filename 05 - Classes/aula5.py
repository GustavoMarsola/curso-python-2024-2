import random
import string

DATABASE = {
    "gustavo.marsola@gmail.com": "teste"
}

CARACTERES_TOKEN = 50

class SistemaHotel:
    # É denominado método inicializador
    # Será executado toda vez que você instanciar sua classe 
    def __init__(self, email: str, senha: str):
        self.email = email
        self.senha = senha
        # O token eu não recebi inicialmente, mas já criei porque vou usá-lo
        self.token    = None
        self.hospedes = []
    
    # Usamos o decorator @staticmethod quando temos uma função na nossa classe que não acessa o atributo self
    @staticmethod
    def gerador_token():
        # Aqui você pode gerar o token de acordo com a sua necessidade
        caracteres = string.ascii_letters + string.digits
        # Gerar o token aleatório
        token = ''.join(random.choice(caracteres) for _ in range(CARACTERES_TOKEN))
        return token
    
    # Autenticar usuário
    def autenticar_usuario(self) -> tuple[bool, str]:
        """
        Esta função acessar o atributo self
        Verifica se o login do usuario está correto
        E retorna um bool que representa o sucesso do login e uma str que é o token
        """
        get_senha = DATABASE.get(self.email)
        if get_senha is None:
            return False, "Email não encontrado"
        
        if get_senha == self.senha:
            self.token = self.gerador_token()
            return True, self.token
        else:
            return False, "Senha incorreta"
    # Registrar um hospede
    def registrar_hospede(self, nome: str, idade: int, quarto: int) -> list:
        # Esta verificação é comumente feita por um decorator também
        if self.token is None:
            print(f"Usuario {self.email} não está autenticado")
            return []
        
        self.hospedes.append(
            {
                "nome": nome,
                "idade": idade,
                "quarto": quarto
            }
        )
        return self.hospedes
    
    # Remover um hospede
    def remover_hospede(self, quarto: int) -> bool:
        if self.token is None:
            print(f"Usuario {self.email} não está autenticado")
            return False
        
        i = 0
        while i < len(self.hospedes):
            hospede = self.hospedes[i]
            if hospede['quarto'] == quarto:
                del self.hospedes[i]  # Remove o hóspede da lista
                print(f"Hóspede no quarto {quarto} removido com sucesso.")
                return True
            i += 1
        
        # Procurar o hóspede no quarto especificado
        # for i, hospede in enumerate(self.hospedes):
        #     if hospede['quarto'] == quarto:
        #         del self.hospedes[i]  # Remove o hóspede da lista
        #         print(f"Hóspede no quarto {quarto} removido com sucesso.")
        #         return True
        
        print(f"Nenhum hóspede encontrado no quarto {quarto}.")
        return False


if __name__ == '__main__':
    sistema = SistemaHotel(email='gustavo.marsola@gmail.com', senha='teste')
    
    login = sistema.autenticar_usuario()
    print(login)
    
    adc_hospede = sistema.registrar_hospede(
        nome='Jose da Silva',
        idade=50,
        quarto=202
    )
    print(adc_hospede)
    