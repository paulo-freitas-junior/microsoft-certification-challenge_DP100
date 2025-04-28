# Pipeline Automação

Neste tópico, vamos explorar e analisar os passos para criação de um pipeline automatizado no Azure ML.

<div align='center'>
    <img src="/images/Projeto01/31_Pipeline01.jpg" width="800">
    <p><strong>Figura 1:</strong> Visão geral da criação do Pipeline</p>
</div>

Na primeira etapa, podemos visualizar o ambiente de criação do pipeline no Azure ML Studio, onde começamos a estruturar nosso fluxo de trabalho automatizado.
Dentro do ambiente de Visão Geral, é possível verificar informações referentes ao Status do experimento, Entrada dos ativos de dados,
Saídas do experimento com informações dos melhores modelos obtidos e dataset de treinamento.

<div align='center'>
    <img src="/images/Projeto01/32_Pipeline02.jpg" width="800">
    <p><strong>Figura 2:</strong> Configuração dos componentes do Pipeline</p>
</div>

Aqui vemos os diferentes componentes sendo organizados no pipeline, incluindo as etapas de processamento de dados e treinamento do modelo.
Pode-se observar também os "trabalhos filhos" do experimento e seus resultados, permitindo ao Cientista de Dados poder optar pelo modelo que obteve o melhor resultado analisando as métricas estatísticas de cada um.

<div align='center'>
    <img src="/images/Projeto01/33_Pipeline03.jpg" width="800">
    <p><strong>Figura 3:</strong> Definição dos parâmetros do Pipeline</p>
</div>

Esta imagem mostra a configuração dos parâmetros específicos de cada componente do pipeline, garantindo o correto fluxo de dados entre as etapas.

<div align='center'>
    <img src="/images/Projeto01/34_Pipeline04.jpg" width="800">
    <p><strong>Figura 4:</strong> Execução do Pipeline</p>
</div>

Podemos observar o resultado as métricas estatísticas de cada etapa de execução do experimento. O Cientista de Dados poderá avaliar 
qual experimento obteve melhores resultados e consequentemente pode selecionar o mesmo para ser inserido em ambiente de Produção.

<div align='center'>
    <img src="/images/Projeto01/35_Pipeline05.jpg" width="800">
    <p><strong>Figura 5:</strong> Monitoramento do Pipeline</p>
</div>

Esta visualização mostra o painel de monitoramento do pipeline, onde podemos acompanhar o progresso e status de cada etapa.
Aqui pode ser definido se o experimento será inserido em um Ponto de Extremidade em Lotes ou de execução em Tempo Real.

<div align='center'>
    <img src="/images/Projeto01/36_Pipeline06.jpg" width="800">
    <p><strong>Figura 6:</strong> Resultado final do Pipeline</p>
</div>

Por fim, vemos o resultado final do pipeline após sua conclusão, com todos os componentes executados com sucesso.