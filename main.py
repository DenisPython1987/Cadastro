from CPF import CPF
from telefone import Telefone as tl
from data import Data
from endereco import Endereco
from Menu import Menu
from banco_de_dados import BancoDeDados as bd
from nome import Nome
from Utilidades.apresentacao import cabeçalho as ca
from Utilidades.apresentacao import linha
from info import Info

cpf_objeto = CPF()
telefone_objeto = tl()
data_objeto = Data()
endereco_objeto = Endereco()
menu_objeto = Menu()
banco_de_dados_objeto = bd()
nome_objeto = Nome()
info_objeto = Info()

while True:
    ca("CADASTRO DE USUÁRIOS")
    print()
    menu_objeto.menu_principal()
    resposta = menu_objeto.escolha_menu()
    if resposta == 1:
        CPF = cpf_objeto.validar_cpf()
        NOME = nome_objeto.validar_nome()
        TELEFONE = telefone_objeto.validar_telefone()
        data_nascimento = data_objeto.data()
        ENDERECO = endereco_objeto.validar_endereco()
        registro = banco_de_dados_objeto.inserir(NOME, TELEFONE, data_nascimento, CPF, ENDERECO)
        if registro > 0:
            linha()
            print("REGISTRO INSERIDO COM SUCESSO!")
        else:
            linha()
            print("NÃO FOI POSSÍVEL CONCLUIR SEU REGISTRO!")
    
    if resposta == 2:
        CPF = cpf_objeto.validar_cpf()
        resultado = banco_de_dados_objeto.buscar_cadastro(CPF)
        linha()
        info_objeto.show_info(resultado)
        
    if resposta == 3:
        retorno = banco_de_dados_objeto.listar_cadastros()
        ca("USUÁRIOS CADASTRADOS")
        info_objeto.listar_info(retorno)
        
    if resposta == 4:
        CPF = cpf_objeto.validar_cpf()
        exclusao = banco_de_dados_objeto.excluir_cadastro(CPF)
        if exclusao:
            print("CADASTRO EXCLUÍDO COM SUCESSO!")
        else:
            print("CADASTRO NÃO ENCONTRADO")
            
    if resposta == 5:
        break
ca("OBRIGADO")
ca("VOLTE SEMPRE!")