-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 21/06/2024 às 20:21
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `malu-projeto`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipes`
--

CREATE TABLE `equipes` (
  `id` int(8) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `localizacao` varchar(15) NOT NULL,
  `potencial` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `equipes`
--

INSERT INTO `equipes` (`id`, `nome`, `localizacao`, `potencial`) VALUES
(9, 'Loud', 'Rio de janeiro', 6),
(10, 'Pain Gaming', 'São Paulo', 2),
(12, 'Ilha das lendas', 'São Paulo', 2),
(13, 'Furia', 'Bahia', 8),
(14, 'INTZ', 'Pernambuco', 9),
(15, 'Fluxo', 'Rio de Janeiro', 7);

-- --------------------------------------------------------

--
-- Estrutura para tabela `resultados_partidas`
--

CREATE TABLE `resultados_partidas` (
  `id` int(11) NOT NULL,
  `equipe1_id` int(11) NOT NULL,
  `equipe2_id` int(11) NOT NULL,
  `equipe1_nome` varchar(255) NOT NULL,
  `equipe2_nome` varchar(255) NOT NULL,
  `pontuacao_equipe1` int(11) DEFAULT NULL,
  `pontuacao_equipe2` int(11) DEFAULT NULL,
  `vencedor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `resultados_partidas`
--

INSERT INTO `resultados_partidas` (`id`, `equipe1_id`, `equipe2_id`, `equipe1_nome`, `equipe2_nome`, `pontuacao_equipe1`, `pontuacao_equipe2`, `vencedor_id`) VALUES
(91, 9, 10, 'Loud', 'Pain Gaming', 4, 0, 9),
(92, 9, 12, 'Loud', 'Ilha das lendas', 3, 1, 9),
(93, 9, 13, 'Loud', 'Furia', 6, 3, 9),
(94, 9, 14, 'Loud', 'INTZ', 2, 3, 14),
(95, 9, 15, 'Loud', 'Fluxo', 4, 2, 9),
(96, 10, 12, 'Pain Gaming', 'Ilha das lendas', 0, 2, 12),
(97, 10, 13, 'Pain Gaming', 'Furia', 0, 7, 13),
(98, 10, 14, 'Pain Gaming', 'INTZ', 2, 4, 14),
(99, 10, 15, 'Pain Gaming', 'Fluxo', 1, 0, 10),
(100, 12, 13, 'Ilha das lendas', 'Furia', 0, 8, 13),
(101, 12, 14, 'Ilha das lendas', 'INTZ', 2, 7, 14),
(102, 12, 15, 'Ilha das lendas', 'Fluxo', 1, 3, 15),
(103, 13, 14, 'Furia', 'INTZ', 7, 4, 13),
(104, 13, 15, 'Furia', 'Fluxo', 7, 5, 13),
(105, 14, 15, 'INTZ', 'Fluxo', 3, 7, 15);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `equipes`
--
ALTER TABLE `equipes`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `resultados_partidas`
--
ALTER TABLE `resultados_partidas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `equipe1_id` (`equipe1_id`),
  ADD KEY `equipe2_id` (`equipe2_id`),
  ADD KEY `vencedor_id` (`vencedor_id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `equipes`
--
ALTER TABLE `equipes`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `resultados_partidas`
--
ALTER TABLE `resultados_partidas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `resultados_partidas`
--
ALTER TABLE `resultados_partidas`
  ADD CONSTRAINT `resultados_partidas_ibfk_1` FOREIGN KEY (`equipe1_id`) REFERENCES `equipes` (`id`),
  ADD CONSTRAINT `resultados_partidas_ibfk_2` FOREIGN KEY (`equipe2_id`) REFERENCES `equipes` (`id`),
  ADD CONSTRAINT `resultados_partidas_ibfk_3` FOREIGN KEY (`vencedor_id`) REFERENCES `equipes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
