from Utilidades.apresentacao import linha

class Info:
    """Classe para lidar com a apresentação de informação"""
    
    def show_info(self, tupla: tuple) -> None:
        """Método para mostrar informações para o usuário"""
        opcoes = ("Nome", "Telefone", "Data de nascimento", "CPF", "Endereço")
        for indice, valor in enumerate(tupla):
            print(f"{opcoes[indice]} = {valor}")
            
    def listar_info(self, lista: list) -> None:
        """Método específico para listar todos os usuários cadastrados"""
        for tupla in lista:
            opcoes = ("Nome", "Telefone", "Data de nascimento", "CPF", "Endereço")
            linha()
            for indice, valor in enumerate(tupla):
                print(f"{opcoes[indice]} = {valor}")
                