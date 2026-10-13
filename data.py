from datetime import datetime

class Data:
    """Classe para lidar com as datas fornecidas pelo usuário"""
    
    
    @staticmethod
    def pegar_data() -> str:
        """Método para pegar a data do usuário"""
        return str(input("Digite sua data de nascimento [dd/mm/aaaa] : "))
    
    
    def validar_data(self, data_str: str, formato: str = "%d/%m/%Y") -> bool:
        """Método para validar a data fornecida pelo usuário"""
        try:
            datetime.strptime(data_str, formato)
            return True
        except ValueError:
            return False
            
            
    def data(self) -> str:
        """Método para retornar a data"""
        while True:
            data_parcial = self.pegar_data()
            data_final = self.validar_data(data_parcial)
            if data_final:
                return data_parcial
            else:
                print("Data inválida. Tente novamente!")
                continue
        