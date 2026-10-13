from Utilidades.apresentacao import cabeçalho as ca
from Utilidades.números import leia_int

class Menu:
    """Classe para representar os menus da aplicação"""
    
    
    def escolha_menu(self) -> int:
        """Método para pegar a opção do usuário"""
        while True:
            opcao = leia_int("Qual é a sua opção (de 1 à 5): ")
            if opcao < 1 or opcao > 5:
                print("Opção inválida. Digite um número de 1 a 5")
                continue
            return opcao
    
    
    def menu_principal(self) -> None:
        """Método para mostrar o menu principal para o usuário"""
        opcoes = (
        "Cadastrar usuário",
        "Buscar usuário",
        "Listar cadastros",
        "Excluir cadastro",
        "Encerrar programa"
        )
        ca("MENU PRINCIPAL")
        for indice, valor in enumerate(opcoes):
            print(f"{indice + 1} - {valor}")
            
            