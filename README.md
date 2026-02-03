Este é um guia técnico para o Sistema de Controle de Competição Esportiva, desenvolvido como projeto final de curso. O sistema utiliza Python e SQL para gerenciar competições no formato de pontos corridos entre 6 a 10 equipes.

Sistema de Controle de Competição Esportiva
Este projeto consiste em uma aplicação robusta para o gerenciamento completo de torneios esportivos. A ferramenta permite desde o cadastro técnico de equipes até a simulação de partidas baseada em algoritmos de probabilidade e a visualização de desempenho através de gráficos estatísticos.

Funcionalidades Principais
1. Gerenciamento de Equipes (CRUD)
O sistema oferece uma interface para controle total das entidades participantes:

Cadastro: Registro de equipes com nome, localização e potencial (valor que indica a probabilidade de vitória).

Consulta: Listagem detalhada de todos os competidores registrados no banco de dados.

Atualização: Alteração de informações cadastrais de equipes existentes.

Exclusão: Remoção definitiva de equipes do sistema.

2. Gestão de Torneio
Sorteio de Partidas: Geração automática de confrontos garantindo que todas as equipes se enfrentem (sistema de todos contra todos).

Simulação de Resultados: As partidas são jogadas automaticamente com pontuações geradas aleatoriamente em função do potencial técnico de cada equipe.

Registro de Resultados: Armazenamento automático dos placares e identificação dos vencedores no banco de dados.

3. Análise de Performance
Visualização de Gráficos: Utilização da biblioteca Matplotlib para gerar gráficos que mostram a evolução da pontuação das equipes ao longo da competição.

Tecnologias Utilizadas
Linguagem: Python 3.

Banco de Dados: MariaDB/MySQL (via PyMySQL).

Interface: Linha de Comando (CLI) para gerenciamento e aplicação Web para visualização.

Bibliotecas:

Matplotlib: Para geração de gráficos de performance.

PyMySQL: Para integração e persistência com o banco de dados [banco_dados.py].

Itertools: Para geração de combinações de partidas [main.py].

Estrutura do Banco de Dados
O projeto utiliza um esquema relacional com duas tabelas principais:

Tabela equipes: Armazena o ID único, nome, localização e o potencial de cada time.

Tabela resultados_partidas: Registra o histórico de confrontos, IDs das equipes envolvidas, pontuações e o ID do vencedor.

Instalação e Configuração
Clonagem do Repositório:

Bash
git clone https://github.com/augustobmo/lab_social_projeto_final_06-24.git
Configuração do Banco de Dados:

Certifique-se de ter um servidor MySQL/MariaDB ativo.

Importe o esquema contido no arquivo malu-projeto.sql para criar as tabelas necessárias [malu-projeto.sql].

Instalação de Dependências:

Bash
pip install pymysql matplotlib
Execução: Inicie o sistema através do arquivo principal:

Bash
python main.py
[main.py]

Organização do Código
main.py: Contém a lógica do menu principal e o fluxo da competição [main.py].

equipes.py: Implementa a classe Equipe e os métodos de interação com o banco para CRUD [equipes.py].

banco_dados.py: Classe responsável pela conexão e execução de consultas SQL [banco_dados.py].

malu-projeto.sql: Script de criação da estrutura e dados iniciais do banco de dados [malu-projeto.sql].
