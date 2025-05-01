# Playgrounds do Azure AI Studio

Neste guia, vamos explorar o ambiente de Playgrounds do Azure AI Studio, uma ferramenta interativa para experimentação de modelos de IA.

## 1. Página Inicial do Azure AI Studio

<div align="center">
    <img src="/images/Projeto02/19_Playgrounds.jpg" width="800">
    <p><strong>Figura 1:</strong> Dashboard inicial do Azure AI Studio</p>
</div>

O Azure AI Studio oferece uma interface intuitiva para desenvolvimento e teste de soluções de IA. Aqui você encontra:
- Acesso aos diferentes tipos de Playgrounds
- Projetos recentes
- Recursos e documentação
- Métricas de uso

Escolha entre diferentes tipos de Playgrounds:
- Chat (modelos conversacionais)
- Completions (geração de texto)
- DALL-E (geração de imagens)
- Embeddings (vetorização de texto)

## 2. Seleção de Playground de Chat

<div align="center">
    <img src="/images/Projeto02/20_Playgrounds.jpg" width="800">
    <p><strong>Figura 2:</strong> Playground de chat</p>
</div>

Dentro do Playground de Chat é possível definir:
- Modelo de Implementação
- Fornecer instruções de contexto ao modelo
- Adicionar fontes de dados específicas que serão usadas como referência pelo modelo
- Configuração de parâmetros do modelo

Iniciar o chat via Prompt

## 3. Ingestão de dados específicos para o Modelo

<div align="center">
    <img src="/images/Projeto02/21_Playgrounds.jpg" width="800">
    <p><strong>Figura 3:</strong> Interface de fonte de dados</p>
</div>

Área de configuração de ingestão de dados para que a IA Generativa faça referência e dê respostas específicas conforme os dados inseridos no Modelo.
- Inserir dados existentes no ecosistema do Azure
- Inserir dados de fontes externas para o ecosistema do Azure

## 4. Ingestão de dados

<div align="center">
    <img src="/images/Projeto02/22_Playgrounds.jpg" width="800">
    <p><strong>Figura 4:</strong> Ingestão por tipos de arquivos</p>
</div>

A ingestão dos dados tem como padrões:
- Arquivos nos formatos listados com limite de 16MB cada
- Geração de índices dos dados para que o modelo localize de forma rápida e precisa as informações


## 5. Configuração dos Índices de Dados

<div align="center">
    <img src="/images/Projeto02/23_Playgrounds.jpg" width="800">
    <p><strong>Figura 5:</strong> Visualização do histórico de chat</p>
</div>

Seção onde-se cria um Recurso de Pesquisa da IA caso não exista uma já definida e onde o é gerado o índice de vetores com as informações dos dados que foram inseridos no modelo

## 6. Criação do Serviço de Pesquisa

<div align="center">
    <img src="/images/Projeto02/24_Playgrounds.jpg" width="800">
    <p><strong>Figura 6:</strong> Interface de criação do serviço</p>
</div>

Processo de criação do Serviço de Pesquisa consiste:
- Detalhamento do Projeto
    - Tipo de assinatura do Azure
    - Grupo de recurso a ser utilizado pelo Serviço de Pesquisa

- Detalhes da Instância
    - Nome do Serviço criado para ChatBot
    - Localização do Servidor do serviço criado
    - Tipo de Preço do Recurso que será cobrado para uso

## 7. Tabela de Preços do Recurso de Pesquisa

<div align="center">
    <img src="/images/Projeto02/25_Playgrounds.jpg" width="800">
    <p><strong>Figura 7:</strong> Painel informação de preços</p>
</div>

Tabela contendo a informação de preços conforme o tipo de SKU oferecido no Azure
A escolha do SKU depende da dimensão do Projeto que está sendo implementado

## 8. Implementação do Recurso de Pesquisa Selecionado

<div align="center">
    <img src="/images/Projeto02/26_Playgrounds.jpg" width="800">
    <p><strong>Figura 8:</strong> Definição do Recurso</p>
</div>

- Detalhes do Projeto:
    - Assinatura da subscription no Azure
    - Grupo de recurso para o projeto

- Detalhes da Instância
    - Nome do Serviço
    - Localização do Servidor de hospadgem do serviço
    - Tipo de preço selecionado do serviço

## 9. Confirmação de implementação do Recurso

<div align="center">
    <img src="/images/Projeto02/27_Playgrounds.jpg" width="800">
    <p><strong>Figura 9:</strong> Informações sobre implementação</p>
</div>

Fornece os detalhes da implantação do Recurso solicitado.
- Assinatura da subscription
- Grupo de recurso do Projeto selecionado
- Detalhes da implantação

## 10. Tela inicial do Recurso de Pesquisa criado

<div align="center">
    <img src="/images/Projeto02/28_Playgrounds.jpg" width="800">
    <p><strong>Figura 10:</strong> Interface do Recurso de Pesquisa do Chatbot</p>
</div>

Contém as informações do serviço de pesquisa criado para o serviço **dio-search-chatbot**

Serviço permite:
- Conectar seus dados através de importação de dados
- Explorar seus dados conectando-se a aplicativos
- Monitorar e dimensionar através de ferramentas 

## 11. Conexão à um recursos de dados existentes

<div align="center">
    <img src="/images/Projeto02/29_Playgrounds.jpg" width="800">
    <p><strong>Figura 11:</strong> Informar o recurso de pesquisa específico para importação</p>
</div>

É informado o nome do recurso de pesquisa onde se encontram os dados que já foram inseridos

## 12. Review das configurações 

<div align="center">
    <img src="/images/Projeto02/30_Playgrounds.jpg" width="800">
    <p><strong>Figura 12:</strong> Configuração</p>
</div>

É possível verificar as informações sobre:
- Configuração de indexação dos dados
- Configurações de pesquisa
- Tipo de conexão de pesquisa
- Se foi realizada a vetorização dos dados (embeddings)

Solicitação de confirmação para criação do índice de vetor

## 13. Monitoramento da criação de Vetores no Playground

<div align="center">
    <img src="/images/Projeto02/31_Playgrounds.jpg" width="800">
    <p><strong>Figura 13:</strong> Playground do Azure - Status de Ingestão</p>
</div>

Processo de criação de índices de vetores dos dados que foram inseridos (RAG) para serem usados como Referência para as consultas via Prompt

## 14. Resultado da criação de Vetores

<div align="center">
    <img src="/images/Projeto02/32_Playgrounds.jpg" width="800">
    <p><strong>Figura 14:</strong> Playground - Arquivo de índice de vetor</p>
</div>

Modelo está preparado usar como referências os dados que foram inseridos (RAG) no ChatBot. 


## 15. Execução do Chatbot

<div align="center">
    <img src="/images/Projeto02/33_Playgrounds.jpg" width="800">
    <p><strong>Figura 15:</strong> Playground - Prompt</p>
</div>

Após a execução de todo o processo é possível verificar o Chatbot em funcionamento e buscando nas fontes de dados específicas (RAG) inseridas, referências de busca baseando-se no que foi solicitado via Prompt.

## Referências

Para mais informações, consulte:

- [Documentação oficial do Azure AI Studio](https://learn.microsoft.com/azure/ai-studio)
- [Guia de início rápido dos Playgrounds](https://learn.microsoft.com/azure/ai-studio/tutorials)
- [Melhores práticas para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/generative-ai)
- [Documentação dos modelos de linguagem](https://learn.microsoft.com/azure/ai-services/openai)
