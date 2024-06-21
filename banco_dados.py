import pymysql

class BancoDeDados:
    def __init__(self, host='localhost', user='root', password='', database='malu-projeto'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexao.cursor()
            print("Conexão estabelecida com sucesso!")
        except pymysql.MySQLError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def executar_consulta(self, consulta, parametros=None):
        try:
            if parametros:
                self.cursor.execute(consulta, parametros)
            else:
                self.cursor.execute(consulta)
            self.conexao.commit()
            return self.cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"Erro ao executar consulta: {e}")
            return None

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
        print("Conexão fechada com sucesso!")
