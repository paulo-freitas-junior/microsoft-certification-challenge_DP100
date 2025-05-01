# Azure AI Services

Processo de criação e configuração do Azure AI Services.

## 1. Acesso ao Azure AI Services

<div align="center">
    <img src="/images/Projeto02/04_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 1:</strong> Página inicial do Azure AI Services</p>
</div>

Azure AI Services oferece uma ampla gama de recursos de inteligência artificial que podem ser facilmente integrados aos seus projetos.

## 2. Criação do Grupo de Recursos

<div align="center">
    <img src="/images/Projeto02/05_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 2:</strong> Criação do grupo de serviço</p>
</div>

Ao iniciar a criação, você será apresentado às opções disponíveis. O Azure AI Services multi-serviço é recomendado para acesso a múltiplos recursos cognitivos em um único recurso.

## 3. Configurações Básicas

<div align="center">
    <img src="/images/Projeto02/06_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 3:</strong> Configurações básicas do serviço</p>
</div>

Configure os detalhes essenciais do seu serviço:
- Subscription: Sua assinatura Azure
- Resource Group: Grupo de recursos criado anteriormente
- Region: Região mais próxima disponível
- Name: Nome único para seu recurso
- Pricing tier: Nível de preço adequado ao seu uso

## 4. Conclusão da Criação do Serviço

<div align="center">
    <img src="/images/Projeto02/07_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 4:</strong> Visão geral da implantação do serviço</p>
</div>

Defina as configurações do serviço, incluindo:
- Re-implantação do serviço
- Detalhes do serviço criado

## 5. Criação de Projetos no Hub

<div align="center">
    <img src="/images/Projeto02/08_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 5:</strong> Configuraççao do Projeto no Hub</p>
</div>

Tela de criação do Projetos dentro do Hub de Projetos para o chatbot.
Permite a configuração das identidades gerenciadas para permitir que o serviço se comunique de forma segura com outros recursos Azure.

## 6. Criação do Projeto

<div align="center">
    <img src="/images/Projeto02/09_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 6:</strong> Criação do Projeto</p>
</div>

Tela de criação do Projeto e dentro do Hub de Projeto selecionado.

## 7. Revisão e Criação

<div align="center">
    <img src="/images/Projeto02/10_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 7:</strong> Visão geral do Projeto Criado</p>
</div>

Visão geral do projeto, contendo a chave de API para requisição via aplicações bem como informações sobre:
- Inferência da IA no Azure
- Pontos de extremidade do do modelo
- Serviços de IA do Azure

## 8. Implementação de Modelos

<div align="center">
    <img src="/images/Projeto02/11_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 8:</strong> Processo de implementação de modelos</p>
</div>

Processo de gerenciamento e implementação de modelos de IA no Azure para o Hub de Projeto criado par ao Chatbot. 
- Suporte a implantação de modelos LLMs
- Fluxos de aplicações Web
- Fluxos implementação futura para ambientes de produção

## 9. Implementação do modelo gpt-4o para o Chatbot

<div align="center">
    <img src="/images/Projeto02/12_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 9:</strong> Escolha do modelo de inferência do chatbot</p>
</div>

Escolha do modelo de IA utilizado para inferência do chatbot. No caso modelo gpt-4o da OpenAI com objetivo de conclusões de chat.
Também é possível verificar as especificidades do modelo.

## 10. Implantação e configuração do modelo gpt-4o 

<div align="center">
    <img src="/images/Projeto02/13_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 10:</strong> Configurações do recurso</p>
</div>

Tela de implantação do modelo permite uma série de configurações:
- Nome do modelo
- Tipo de implementação global
- Detalhes de implementação
    - Permissão de updates do modelo de forma automática
    - Definição do tipo de modelo a ser usado
    - Escolha do Recurso de IA a ser usado
    - Limite de tokenização
    - Definição de filtros de conteúdo

## 11. Overview do Modelo e Pontos de Extremidade

<div align="center">
    <img src="/images/Projeto02/14_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 11:</strong> Resumo das informações da impplementação</p>
</div>

Overview dos recursos criados contendo:
- Pontos de extremidade (URL e chave de acesso)
- Imformações da implementação do modelo (nome, tipo, limites e versão)
- Aplicação do mesmo mediante escolha de uma linguagem para chamadas via API

## 12. Implementação do Embbending

<div align="center">
    <img src="/images/Projeto02/15_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 12:</strong> Seleção do modelo</p>
</div>

Embeddings são representações numéricas que capturam informações sobre palavras, frases ou até mesmo documentos inteiros. Os embeddings são usados para "traduzir" conceitos complexos em algo que um modelo de IA consegue processar.
Os embeedings mapeiam essas palavras em coordenadas nesse espaço, de maneira que palavras ou ideias semelhantes fiquem próximas umas das outras.
- Entender significados
- Gerar conteúdo coerente

## 13. Implantação e Configuração dos Embeddings

<div align="center">
    <img src="/images/Projeto02/16_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 13:</strong> Configurações específicas do serviço</p>
</div>

Configuração da implentação do modelo:
- Nome do modelo
- Tipo de implementação global
- Detalhes de implementação
    - Permissão de updates do modelo de forma automática
    - Versão do modelo
    - Escolha do Recurso de IA a ser usado
    - Limite de tokenização
    - Definição de filtros de conteúdo

## 14. Overview da implementação do Embeddings

<div align="center">
    <img src="/images/Projeto02/17_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 14:</strong> Overview da implementação</p>
</div>

Overview dos recursos criados contendo:
- Pontos de extremidade (URL e chave de acesso)
- Imformações da implementação do modelo (nome, tipo, limites e versão)
- Aplicação do mesmo mediante escolha de uma linguagem para chamadas via API

## 15. Resumo da implementação dos Modelos

<div align="center">
    <img src="/images/Projeto02/18_AzureAI_Foundry.jpg" width="800">
    <p><strong>Figura 15:</strong> Lista de modelos implementados</p>
</div>

Lista de modelos implementados no Hub de Projeto.

---

### Referências

- [O que é Azure AI Services?](https://learn.microsoft.com/pt-br/azure/ai-services/what-are-ai-services)
- [Documentação do Azure AI Services](https://learn.microsoft.com/pt-br/azure/ai-services/)
- [Guia de início rápido: Criar um recurso do Azure AI Services](https://learn.microsoft.com/pt-br/azure/ai-services/multi-service-resource?tabs=windows&pivots=programming-language-csharp)
- [Segurança e conformidade no Azure AI Services](https://learn.microsoft.com/pt-br/azure/ai-services/security-features)
- [Preços do Azure AI Services](https://azure.microsoft.com/pt-br/pricing/details/cognitive-services/)
