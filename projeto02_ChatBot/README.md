# Projeto 02 - ChatBot com Arquitetura RAG

[![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)](https://github.com/SEU_USUARIO/SEU_REPOSITORIO)
[![Licença](https://img.shields.io/badge/licença-MIT-blue)](https://github.com/SEU_USUARIO/SEU_REPOSITORIO/blob/main/LICENSE)

<div align="center">
  <img src="/images/projeto2_logo.jpg" width="25%" alt="Capa do Projeto ChatBot">
</div>

## 📋 Sumário
- [Sobre o Projeto](#sobre-o-projeto)
- [Cenário](#cenário)
- [Objetivos](#objetivos)
- [Arquitetura da Solução](#arquitetura-da-solução)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)

## 🎯 Sobre o Projeto
Neste projeto, será desenvolvido um chatbot interativo capaz de responder perguntas com base em documentos PDF carregados pelo usuário dentro da plataforma do Azure AI Foundry. O sistema utiliza uma arquitetura RAG (Retrieval-Augmented Generation) para processar, indexar e recuperar informações relevantes dos documentos.

## 📚 Cenário
Um estudante de Engenharia de Software necessita analisar diversos artigos científicos para seu TCC. Com o acúmulo de documentos, torna-se desafiador extrair e correlacionar informações relevantes entre os textos. A solução proposta utiliza IA para criar um sistema de busca inteligente que interpreta PDFs e gera respostas contextualizadas.

## ✅ Objetivos
- Implementar carregamento e processamento de arquivos PDF
- Desenvolver sistema de busca vetorial para indexação
- Integrar IA generativa para geração de respostas
- Criar interface de chat interativa
- Garantir respostas fundamentadas no conteúdo dos documentos

## 🏗️ Arquitetura da Solução
```
[PDF Documents] → [Text Extraction] → [Vector Embeddings] → [Vector Database]
                                                                ↓
[User Query] → [Query Processing] → [Vector Search] → [Context Retrieval] → [LLM Response]
```

## 🔧 Tecnologias Utilizadas
*   Microsoft Azure
*   Microsoft Azure Machine Learning
*   Azure OpenAI Service
*   Linguagem Python V. 3.12
*   Azure SDK for Python
*   Jupyter Notebooks

## 🚀 Como Executar
1. Configure o ambiente Azure:
```bash
az login
az group create --name rg-chatbot-dev --location eastus
```

2. Configure as variáveis de ambiente:
```bash
AZURE_OPENAI_KEY=sua_chave
AZURE_OPENAI_ENDPOINT=seu_endpoint
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o aplicativo:
```bash
python src/main.py
```

## 📁 Estrutura do Projeto

<b> Subdivido em 3 tópicos por pastas para melhor entendimento e leitura do projeto </b>

1. [Resource Group no Azure](/projeto02_ChatBot/01-ResourceGroup/ResourceGroup.md)
2. [Azure AI Foundry](/projeto02_ChatBot/02-AzureAI_Foundry/AzureAI_Foundry.md)
3. [Playgrounds](/projeto02_ChatBot/03-Playgrounds/Playgrounds.md)

## 📂 Pastas <a name="pastas"></a>

| Pasta     | Descrição                                                   |
| --------- | ----------------------------------------------------------- |
| database  | Possui as bases de dados usadas nos projetos                |
| inputs    | Possui arquivos referentes aos levantamentos a serem feitos |
| scripts   | Possui scripts em Python com execução de testes adicionais. |
| projetos  | 03 pastas de projetos separados pelos tópicos acima         |

## 📝 Notas de Implementação
- O sistema utiliza embeddings para criar representações vetoriais do texto
- Implementa cache para otimizar consultas frequentes
- Mantém rastreabilidade das fontes nas respostas
- Utiliza chunking eficiente para processamento de documentos longos

## 📄 Licença
Este projeto está sob a licença MIT.