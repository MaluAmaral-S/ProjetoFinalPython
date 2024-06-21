from banco_dados import BancoDeDados
import random
'''
CREATE TABLE `equipes` (
  `id` int(8) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `localizacao` varchar(15) NOT NULL,
  `potencial` float NOT NULL
);
'''

class Equipe:
    def __init__(self, id, nome, localizacao, potencial):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao
        self.potencial = potencial

    @staticmethod
    def obter_todos():
        bd = BancoDeDados()
        bd.conectar()
        consulta = "SELECT * FROM equipes"
        resultados = bd.executar_consulta(consulta)
        bd.fechar_conexao()
        return [Equipe(*resultado) for resultado in resultados]

    @classmethod
    def criar(cls, nome, localizacao):
        potencial = random.randint(1, 10)  # Gerando potencial aleatório de 1 a 10
        bd = BancoDeDados()
        bd.conectar()
        consulta = "INSERT INTO equipes (nome, localizacao, potencial) VALUES (%s, %s, %s)"
        bd.executar_consulta(consulta, (nome, localizacao, potencial))
        bd.fechar_conexao()

    def atualizar(self, novo_nome, nova_localizacao):
        bd = BancoDeDados()
        bd.conectar()
        consulta = "UPDATE equipes SET nome=%s, localizacao=%s WHERE id=%s"
        bd.executar_consulta(consulta, (novo_nome, nova_localizacao, self.id))
        bd.fechar_conexao()
        # Atualizar os atributos do objeto após atualização no banco, se necessário
        self.nome = novo_nome
        self.localizacao = nova_localizacao

    def apagar(self):
        bd = BancoDeDados()
        bd.conectar()
        consulta = "DELETE FROM equipes WHERE id=%s"
        bd.executar_consulta(consulta, (self.id,))
        bd.fechar_conexao()
        # Opcionalmente, limpar ou invalidar o objeto após a exclusão

    def sortear_potencial(self):
        novo_potencial = random.randint(1, 10)
        self.potencial = novo_potencial
        # Atualizar no banco de dados
        bd = BancoDeDados()
        bd.conectar()
        consulta_atualizar = "UPDATE equipes SET potencial = %s WHERE id = %s"
        parametros = (novo_potencial, self.id)
        bd.executar_consulta(consulta_atualizar, parametros)
        bd.fechar_conexao()
