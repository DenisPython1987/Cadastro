

class CPF:
    """Classe para lidar com a validação do CPF do programa"""
    @staticmethod
    def pega_cpf() -> str:
        """Método para pegar o CPF do usuário"""
        return str(input("Digite o CPF: ")).strip()
        
    
    @staticmethod
    def verificar_cpf(cpf: str) -> str:
        """Método para validar o CPF
        Parâmetro cpf: string"""
        parcial = cpf.replace(",", "").replace(".", "").replace("-", "").replace("/", "")
        if len(parcial) != 11:
            print("Número de CPF inválido")
            return False
        else:
            return parcial
            
    
    @staticmethod
    def validar_inteiros_cpf(cpf: str) -> str:
        """Método para verifiar se todos os caracteres do CPF são números inteiros"""
        try:
            for valor in cpf:
                int(valor)
        except (ValueError, TypeError):
            print("Número de CPF inválido")
            return False
        else:
            return cpf
            
    @staticmethod
    def verificar_iguais(cpf: str) -> str:
        """ método para verificar se todos os digitos são iguais.
        Parâmetro cpf: string com os dados"""
        if cpf == cpf[0] * 11:
            return False
        else:
            return cpf
            
            
    @staticmethod
    def verificar_primeiro_dig(cpf: str) -> bool:
        """Método para verificar o primeiro dígito verificador do CPF.
        Parâmetro cpf: int"""
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        digito_1 = resto if resto < 10 else 0
        return int(cpf[9]) == digito_1
            
            
    @staticmethod
    def verifica_segundo_dig(cpf: str) -> bool:
        """ Método para verificar o segundo dígito do CPF.
        Parâmetro cpf: int"""
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        digito_2 = resto if resto < 10 else 0
        return int(cpf[10]) == digito_2
        
            
    def validar_cpf(self) -> str:
        """ Método final para validar o cpf"""
        while True:
            cpf_1 = self.pega_cpf()
            cpf_2 = self.verificar_cpf(cpf_1)
            if not cpf_2 or len(cpf_2) == 0:
                print("Tente novamente")
                continue
            else:
                cpf_3 = self.validar_inteiros_cpf(cpf_2)
            if not cpf_3:
                print("Tente novamente")
                continue
            else:
                cpf_4 = self.verificar_iguais(cpf_3)
            cpf_6 = self.verificar_primeiro_dig(cpf_4)
            cpf_7 = self.verifica_segundo_dig(cpf_4)
            if cpf_6 and cpf_7:
                return str(cpf_4)
            else:
                print("CPF inválido. Tente novamente")
                continue
                