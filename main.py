from equipes import Equipe  # Importe sua classe Equipe aqui
import random
from itertools import combinations
from banco_dados import BancoDeDados
import matplotlib.pyplot as plt

# Função para sortear as partidas
def sortear_partidas(banco):
    # Apagar as informações antigas da tabela resultados_partidas
    try:
        consulta_apagar = "DELETE FROM resultados_partidas"
        banco.executar_consulta(consulta_apagar)
        print("Informações antigas apagadas com sucesso!")
    except Exception as e:
        print(f"Erro ao apagar informações antigas: {e}")

    equipes = Equipe.obter_todos()
    partidas = list(combinations(equipes, 2))  # Gera todas as combinações possíveis de 2 equipes

    try:
        for equipe1, equipe2 in partidas:
            # Inserir partida na tabela resultados_partidas
            consulta_inserir = "INSERT INTO resultados_partidas (equipe1_id, equipe2_id, equipe1_nome, equipe2_nome) VALUES (%s, %s, %s, %s)"
            parametros = (equipe1.id, equipe2.id, equipe1.nome, equipe2.nome)
            banco.executar_consulta(consulta_inserir, parametros)

        print("Partidas sorteadas e adicionadas ao banco de dados com sucesso!")

    except Exception as e:
        print(f"Erro ao sortear e adicionar partidas: {e}")

    return partidas

# Função para exibir as partidas sorteadas
def exibir_partidas(partidas):
    for i, partida in enumerate(partidas, 1):
        equipe1, equipe2 = partida
        print(f"Partida {i}: {equipe1.nome} vs {equipe2.nome}")

# Função para jogar a próxima partida e registrar o resultado
def jogar_proxima_partida(partidas, banco):
    if not partidas:
        print("Nenhuma partida sorteada. Por favor, sorteie as partidas primeiro.")
        return [], 0

    equipe1, equipe2 = partidas[0]
    potencial_equipe1 = equipe1.potencial
    potencial_equipe2 = equipe2.potencial

    # Simulação de resultados (exemplo: usando randint para pontuações)
    pontuacao_equipe1 = random.randint(0, potencial_equipe1)
    pontuacao_equipe2 = random.randint(0, potencial_equipe2)

    # Determinando o vencedor com base na pontuação
    if pontuacao_equipe1 > pontuacao_equipe2:
        vencedor = equipe1
    elif pontuacao_equipe2 > pontuacao_equipe1:
        vencedor = equipe2
    else:
        print("Empate! Não há vencedor definido.")
        return partidas, 0

    try:
        # Atualizar o resultado da partida na tabela resultados_partidas
        consulta_atualizar = "UPDATE resultados_partidas SET pontuacao_equipe1 = %s, pontuacao_equipe2 = %s, vencedor_id = %s WHERE equipe1_id = %s AND equipe2_id = %s"
        parametros = (pontuacao_equipe1, pontuacao_equipe2, vencedor.id, equipe1.id, equipe2.id)
        banco.executar_consulta(consulta_atualizar, parametros)

        print("Partida registrada no banco de dados com sucesso!")
        print(f"Resultado: {equipe1.nome} {pontuacao_equipe1} x {pontuacao_equipe2} {equipe2.nome}")

        # Remover a partida jogada da lista de partidas
        partidas.pop(0)

        # Contar partidas restantes
        partidas_restantes = contar_partidas_restantes(partidas)
        print(f"Partidas restantes: {partidas_restantes}")

    except Exception as e:
        print(f"Erro ao registrar partida: {e}")

    return partidas, partidas_restantes

# Função para jogar todas as partidas de uma vez
def jogar_todas_partidas(partidas, banco):
    partidas_restantes = len(partidas)
    while partidas:
        partidas, partidas_restantes = jogar_proxima_partida(partidas, banco)

    if partidas_restantes == 0:
        print("Todas as partidas foram jogadas.")

# Função para contar as partidas restantes
def contar_partidas_restantes(partidas):
    return len(partidas)

# Função para obter a performance das equipes
def obter_performance_equipes(banco):
    try:
        consulta = "SELECT equipe1_nome, equipe2_nome, pontuacao_equipe1, pontuacao_equipe2 FROM resultados_partidas"
        resultados = banco.executar_consulta(consulta)
        performance_equipes = {}

        for resultado in resultados:
            equipe1_nome, equipe2_nome, pontuacao_equipe1, pontuacao_equipe2 = resultado
            if equipe1_nome not in performance_equipes:
                performance_equipes[equipe1_nome] = 0
            if equipe2_nome not in performance_equipes:
                performance_equipes[equipe2_nome] = 0

            performance_equipes[equipe1_nome] += pontuacao_equipe1
            performance_equipes[equipe2_nome] += pontuacao_equipe2

        return performance_equipes

    except Exception as e:
        print(f"Erro ao obter performance das equipes: {e}")
        return None

# Função para plotar o gráfico de performance por equipe
def plotar_grafico_performance(performance_equipes):
    if not performance_equipes:
        print("Nenhuma informação de performance disponível.")
        return

    equipes = list(performance_equipes.keys())
    pontuacoes = [performance_equipes[equipe] for equipe in equipes]

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.barh(equipes, pontuacoes, color='skyblue')
    plt.xlabel('Pontuação')
    plt.ylabel('Equipes')
    plt.title('Pontuação das Equipes')
    plt.tight_layout()
    plt.show()

# Função principal que gerencia o menu
def main():
    banco = BancoDeDados()  # Instância do banco de dados
    banco.conectar()  # Conecta ao banco de dados

    partidas = []
    while True:
        print("\n1. Gerenciar Equipes")
        print("2. Sortear Partidas")
        print("3. Visualizar Partidas")
        print("4. Jogar a Próxima Partida")
        print("5. Jogar Todas as Partidas")
        print("6. Ver Gráfico de Performance por Equipe")
        print("7. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
         gerenciar_equipes(banco)
        elif choice == '2':
            partidas = sortear_partidas(banco)
            print("Partidas sorteadas com sucesso!")
            exibir_partidas(partidas)
        elif choice == '3':
            if partidas:
                exibir_partidas(partidas)
            else:
                print("Nenhuma partida sorteada. Por favor, sorteie as partidas primeiro.")
        elif choice == '4':
            partidas, partidas_restantes = jogar_proxima_partida(partidas, banco)
            if partidas_restantes == 0:
                print("Todas as partidas foram jogadas.")
        elif choice == '5':
            jogar_todas_partidas(partidas, banco)
        elif choice == '6':
            # Ver Gráfico de Performance
            performance_equipes = obter_performance_equipes(banco)
            plotar_grafico_performance(performance_equipes)
        elif choice == '7':
            banco.fechar_conexao()  # Fecha a conexão com o banco de dados
            break
        else:
            print("Opção inválida. Tente novamente.")

    banco.fechar_conexao()  # Em caso de saída do loop, garante que a conexão seja fechada

# Função para gerenciar equipes (suponho que você já tenha implementado essa função)
def gerenciar_equipes(banco):
    while True:
        print("\nGerenciamento de Equipes")
        print("1. Ver Equipes Cadastradas")
        print("2. Cadastrar Equipe")
        print("3. Atualizar Equipe")
        print("4. Apagar Equipe")
        print("5. Sortear Novo Potencial para uma Equipe")
        print("6. Voltar")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            equipes = Equipe.obter_todos()
            for equipe in equipes:
                print(f"ID: {equipe.id}, Nome: {equipe.nome}, Localização: {equipe.localizacao}, Potencial: {equipe.potencial}")
        elif choice == '2':
            nome = input("Nome do Time: ")
            localizacao = input("Localização (Estado ou País): ")
            Equipe.criar(nome, localizacao)
            print(f'Equipe {nome} cadastrada com sucesso')
        elif choice == '3':
            equipes = Equipe.obter_todos()
            for equipe in equipes:
                print(f"ID: {equipe.id}, Nome: {equipe.nome}, Localização: {equipe.localizacao}, Potencial: {equipe.potencial}")
            equipe_id = input("ID da Equipe a ser atualizada: ")
            equipe_para_atualizar = next((equipe for equipe in equipes if equipe.id == int(equipe_id)), None)
            if equipe_para_atualizar:
                novo_nome = input("Novo nome do Time: ")
                nova_localizacao = input("Nova localização (Estado ou País): ")
                equipe_para_atualizar.atualizar(novo_nome, nova_localizacao)
                print(f'Equipe {novo_nome} atualizada com sucesso')
            else:
                print("Equipe não encontrada")
        elif choice == '4':
            equipes = Equipe.obter_todos()
            for equipe in equipes:
                print(f"ID: {equipe.id}, Nome: {equipe.nome}, Localização: {equipe.localizacao}, Potencial: {equipe.potencial}")
            equipe_id = input("ID da Equipe a ser apagada: ")
            equipe_para_apagar = next((equipe for equipe in equipes if equipe.id == int(equipe_id)), None)
            if equipe_para_apagar:
                confirmacao = input(f"Tem certeza que deseja apagar a equipe {equipe_para_apagar.nome}? (s/n): ")
                if confirmacao.lower() == 's':
                    equipe_para_apagar.apagar()
                    print(f'Equipe {equipe_para_apagar.nome} apagada com sucesso')
                else:
                    print("Operação cancelada")
            else:
                print("Equipe não encontrada")
        elif choice == '5':
            equipes = Equipe.obter_todos()
            for equipe in equipes:
                print(f"ID: {equipe.id}, Nome: {equipe.nome}, Localização: {equipe.localizacao}, Potencial: {equipe.potencial}")
            equipe_id = input("ID da Equipe para sortear novo potencial: ")
            equipe_para_sortear = next((equipe for equipe in equipes if equipe.id == int(equipe_id)), None)
            if equipe_para_sortear:
                equipe_para_sortear.sortear_potencial()
                print(f"Novo potencial da equipe {equipe_para_sortear.nome}: {equipe_para_sortear.potencial}")
            else:
                print("Equipe não encontrada")
        elif choice == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa principal
if __name__ == "__main__":
    main()
