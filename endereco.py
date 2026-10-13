import re
import requests

class Endereco:
    """Classe para lidar com o endereço"""
    
    
    @staticmethod
    def pegar_cep() -> str:
        """Método para pegar o CEP do usuário"""
        return str(input("Digite o seu CEP (somente números): "))
        
    
    @staticmethod
    def polir_cep(cep: str) -> str:
        """Método para limpar a fomatação do CEP"""
        cep_limpo = re.sub(r'\D', ' ', cep)
        return cep_limpo
        
    @staticmethod
    def verifica_tamanho(cep: str) -> str:
        """Método para verificar o tamanho do CEP"""
        if len(cep) != 8:
            print("CEP inválido, tente novamente")
            return False
        else:
            return cep
            
    @staticmethod
    def consulta_cep(cep: str) -> dict | None:
        """Método que busca o cep na Viacep e retorna o resultado ou None"""
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                return dados
            print("CEP não encontrado na base de dados")
            return None
            
    @staticmethod
    def confirmacao() -> str:
            """Método para confirmar o endereço"""
            while True:
                try:
                    resposta = str(input("Esse endereço está correto? [S/N]: ")).strip().upper()[0]
                    if resposta in "SN":
                        return resposta
                    else:
                        print("Resposta inválida. Responda apenas S ou N")
                        continue
                except IndexError:
                    print("A resposta não podw ficar vazia")
                    continue
            
            
    def validar_endereco(self) -> str | None:
        """Método para coletar, validar e retornar o CEP"""
        while True:
            cep_1 = self.pegar_cep()
            cep_2 = self.polir_cep(cep_1)
            cep_3 = self.verifica_tamanho(cep_2)
            if cep_3:
                cep_4 = self.consulta_cep(cep_3)
                if cep_4:
                    endereco = (f"Logradouro: {cep_4['logradouro']}\n"
                    f"Bairro: {cep_4['bairro']}\n"
                    f"Localidade: {cep_4['localidade']}\n"
                    f"UF: {cep_4['uf']}\n")
                    print(endereco)
                    resposta = self.confirmacao()
                    if resposta == 'S':
                        return endereco
                    else:
                        print("Vamos tentar novamente?")
                        continue
                    while True:
                        print(endereco)
                else:
                    continue
            else:
                continue