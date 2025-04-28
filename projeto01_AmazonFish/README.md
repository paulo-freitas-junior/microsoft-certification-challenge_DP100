# Projeto AmazonFish - Previsão de vendas com autoML 🎣

[![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)](https://github.com/SEU_USUARIO/SEU_REPOSITORIO)
[![Licença](https://img.shields.io/badge/licença-MIT-blue)](https://github.com/SEU_USUARIO/SEU_REPOSITORIO/blob/main/LICENSE)

<div align="center">
  <img src="/images/projeto1_logo.jpeg" width="25%" alt="Capa do Projeto AmazonFish">
</div>

## 📝 Índice

*   [Contexto](#contexto)
*   [Objetivo](#objetivo)
*   [Etapas](#etapas)
*   [Estrutura](#estrutura)
*   [Pastas](#pastas)
*   [Tecnologias](#tecnologias)
*   [Contribuição](#contribuição)
*   [Licença](#licença)

## 📚 Contexto <a name="contexto"></a>

AmazonFish Equipamentos é uma empresa inovadora especializada na venda de equipamentos de pesca esportiva. Fundada há 15 anos, a empresa começou como uma pequena loja física em Florianópolis, mas rapidamente expandiu para o mercado digital, tornando-se uma referência nacional em produtos de alta performance para pescadores amadores e profissionais.
Atualmente, a AmazonFish opera por meio de um e-commerce robusto, oferecendo desde varas, iscas e molinetes até tecnologia embarcada, como sonares e GPS para embarcações. Seu diferencial está na experiência do consumidor: a empresa usa dados para entender as necessidades dos clientes e oferecer produtos sob medida.

## 🎯 Objetivo <a name="objetivo"></a>

  - Treinar um modelo de machine learning para prever a venda de equipamentos de pesca
  - Registrar e gerenciar o modelo usando o MlFlow
  - Implementar o modelo para previsões em tempo real em um ambiente de cloud computing
  - Criar um Pipeline estruturado para treinar e testar o modelo, garantindo reprodutibilidade

## 👣 Etapas <a name="etapas"></a>

- Preparação do ambiente do Azure Machine Learning
- Configuração dos recursos computacionais necessários (Instâncias e Clusters)
- Inserção de ativos de dados e definição do tipo de armazenamento a ser escolhido
- Criação de um trabalho de ML automatizado com a escolha do modelo preditivo de ML mais adequado

## 🗂️ Estrutura <a name="estrutura"></a>

<b> Subdividido em 12 tópicos separados por pastas para melhor entendimento e leitura do projeto </b>

1. [Resource Group no Azure](/projeto01_AmazonFish/01-Resource_Groups/Resource_group.md)
2. [Machine Learning](/projeto01_AmazonFish\02-Machine_Learning\Machine_Learning.md)
3. [Workspaces no Azure](/projeto01_AmazonFish\03-Workspaces\Workspaces.md)
4. [Notebooks no Azure Machine Learning](/projeto01_AmazonFish\04-Notebooks\Notebooks.md)
5. [Computação no Azure](/projeto01_AmazonFish\05-Computacao_Azure\ComputacaoAzure.md)
6. [Computação para Notebooks no Azure Machine Learning](/projeto01_AmazonFish\06-Computacao_Notebooks\ComputacaoNotebooks.md)
7. [Computação para Clusters no Azure Machine Learning](/projeto01_AmazonFish\07-Computacao_Clusters\ComputacaoClusters.md)
8. [Dados](/projeto01_AmazonFish\08-Dados\Dados.md)
9. [Auto Machine Learning (autoML) no Azure Machine Learning](/projeto01_AmazonFish\09-AutoML\AutoML.md)
10. [Designer no Azure Machine Learning](/projeto01_AmazonFish\10-Designer\Designer.md)
11. [Jobs no Azure Machine Learning](/projeto01_AmazonFish\11-Jobs\Jobs.md)
12. [Pipeline de automação no Azure Machine Learning](/projeto01_AmazonFish\12-Pipeline_Automacao\Pipeline.md)

## 📂 Pastas <a name="pastas"></a>

| Pasta     | Descrição                                                   |
| --------- | ----------------------------------------------------------- |
| database  | Possui as bases de dados usadas nos projetos                |
| inputs    | Possui arquivos referentes aos levantamentos a serem feitos |
| scripts   | Possui scripts em Python com execução de testes adicionais. |
| projetos  | 12 pastas de projetos separados pelos tópicos acima         |

## 🛠️ Tecnologias <a name="tecnologias"></a>

*   Microsoft Azure
*   Microsoft Azure Machine Learning
*   Microsoft Blob Storage
*   Linguagem Python V. 3.12
*   Jupyter Notebooks

## 📜 Licença <a name="licença"></a>

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.