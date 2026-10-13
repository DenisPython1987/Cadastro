

class Telefone:
    """Classe para lidar com a coleta do número de telefone do usuário"""
    
    
    @staticmethod
    def pegar_telefone() -> str:
        """Método para pegar o número de telefone do usuário"""
        return str(input("Digite seu número de telefone: +55 ")).strip()
  
        
    @staticmethod
    def remover_simbolos(telefone: str) -> str:
       """Método para remover os caracteres especiais da string do número de telefone"""
       return telefone.replace("(", "").replace(")", "").replace("-", "")
    
    
    @staticmethod
    def tamanho(telefone: str) -> str:
        """Método paea verificar o tamanho do número de telefone"""
        if len(telefone) != 11:
            print("Número de telefone inválido. Tente novamente!")
            return False
        else:
            return telefone
    
    
    @staticmethod
    def verifica_int(telefone: str) -> str:
        """Método para verificar se o usuário digitou somente números"""
        try:
            for caractere in telefone:
                int(caractere)
        except (TypeError, ValueError):
            print("Número de telefone inválido. Tente novamente.")
            return False
        else:
            return telefone
        
        
    def validar_telefone(self) -> str:
        """Método para validar o número de telefone"""
        while True:
            numero = self.pegar_telefone()
            numero_1 = self.remover_simbolos(numero)
            numero_2 = self.tamanho(numero_1)
            if not numero_2:
                continue
            else:
                numero_3 = self.verifica_int(numero_2)
                if not numero_3:
                    continue
                else:
                    return f"+55{numero_3}"
        