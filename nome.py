import re

class Nome:
    """Classe para lidar com os dados do programa"""
    
    @staticmethod
    def pegar_nome() -> str:
        """Método para pegar o nome do usuário"""
        return str(input("Digite o seu nome: ")).strip()
        
    @staticmethod
    def verifica_nome(nome: str) -> bool:
        """Método para verificar se o nome contém apenas letras"""
        padrao = r"^[A-Za-zÀ-\u00ff\s-]+$"
        return bool(re.fullmatch(padrao, nome))
        
        
    def validar_nome(self) -> str:
        """Método para validar o nome do usuário.
        Parâmetro nome: string"""
        while True:
            nome = self.pegar_nome()
            if not nome:
                print("O nome não pode ficar vazio. Tente novamente.")
                continue
            resultado = self.verifica_nome(nome)
            if resultado:
                return nome
        
        