import sqlite3

class BancoDeDados:
    """Classe para cuidar do banco de dados"""
    def __init__(self, nome_do_banco: str = "cadastro.db") -> None:
        self.nome_do_banco = nome_do_banco
        self.criar_tabela()
        
        
    def conectar(self) -> sqlite3.Connection:
        """Método para conectar o banco de dados"""
        return sqlite3.connect(self.nome_do_banco)
        
        
    def criar_tabela(self) -> None:
        """Método que garante que o banco exista antes de inserir dados"""
        with self.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
            """CREATE TABLE IF NOT EXISTS dados_clientes(
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL)""")
            
            
    def inserir(self, nome: str, telefone: str,
     data_nascimento: str, cpf: str, endereco: str) -> None:
        """Método CREATE para criar um registro no banco de dados"""
        try:
            with self.conectar() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                "INSERT INTO dados_clientes"
                "(nome, telefone, data_nascimento, cpf, endereco)"
                "VALUES (?, ? ,? ,? ,?)", (nome, telefone, data_nascimento, cpf, endereco))
        except sqlite3.IntegrityError:
            print("Não é permitido usar o mesmo CPF para mais de um cadastro")
        except Exception as erro:
            print(f"Infelizmente tivemos o erro {erro}")
        else:
            conexao.commit()
        return cursor.lastrowid
            
            
    def listar_cadastros(self) -> list[tuple]:
        """Método READ que retorna uma lista de tuplas onde, 
        cada tupla são os dados de um cadastro"""
        with self.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
            "SELECT nome, telefone, data_nascimento, cpf, endereco FROM dados_clientes")
            return cursor.fetchall()
            
            
    def buscar_cadastro(self, cpf: str) -> list[tuple]:
        """Método READ para buscar um cadastro em específico"""
        with self.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
            "SELECT nome, telefone, data_nascimento, cpf, endereco "
            "FROM dados_clientes WHERE cpf = ?", (cpf,))
            return cursor.fetchone()
            
            
    def alterar_cadastro(self, nome: str, telefone: str,
     data_nascimento: str, cpf: str, endereco: str) -> None:
         """Método para atualizar o bancobde dados"""
         with self.conectar() as conexao:
             cursor = conexao.cursor()
             cursor.execute(
             "UPDATE dados_clientes SET nome = ?,"
             " telefone = ?, data_nascimento = ?,"
             " endereco =? WHERE cpf = ? ", (nome,
             telefone, data_nascimento, endereco, cpf))
             conexao.commit()
             return cursor.rowcount > 0
              
              
    def excluir_cadastro(self, cpf: str) -> None:
        """Método para excluir um cadastro
      parâmetro cpf: chave primária do
       cadastro"""
        with self.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
           "DELETE FROM dados_clientes WHERE cpf = ?", (cpf,))
            conexao.commit()
            return cursor.rowcount > 0
            