# health_insurance_cross_sell
![1140-couple-completing-insurance-application-online](https://user-images.githubusercontent.com/98356094/157327525-535220d8-4d37-4ba2-88f6-604e6ada1736.jpeg)


Este é um projeto realizado com dados públicos disponibilizados pela empresa na plataforma do [KAGGLE](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction).


## 1. Problema de Negócio
Nosso cliente, uma Seguradora que fornece Seguro Saúde para seus clientes, têm interesse em oferecer aos seus segurados seguro de veículos. Diante disso, precisam de uma solução para prever se seus clientes do ano passado terão interesse no seguro veicular fornecido pela empresa, levando em consideração o recurso humano limitado que possuem, com um número de time de vendas com capacidade em realizar apenas 20 mil ligações no período da campanha.

## 2. Entendimento do Negócio
#### Motivação
A empresa fez uma pesquisa, no ano passado, com seus clientes e obteve dados sobre o interesse ou não em adiquirir o seguro de automóvel.

#### Causa Raiz do Problema
O time de produtos está analisando a possibilidade em oferecer um novo produto aos segurados.

#### Quem é o Stakeholder
o time de produtos da empresa.


#### Formato da Solução
* Planilha na plataforma Google
* Modelo de classificação para um problema Learning to Rank.
 
 
## 3. Metodologia de Desenvolvimento do Projeto
 O projeto está sendo desenvolvido pela técnica CRISP-DM
 * Versão END-TO_END da solução,
 * Velocidade na entrega de valor,
 * Mapeamento de todos os possíveis problems.


##### Passo 01 - Descrição dos dados: Conhecimento dos dados, tipos, métricas estatísticas para identificar outliers, analise das métricas estatísticas e ajustes em features do dataset (preenchimento de NA's).


##### Passo 02 - Feature Engineering: Desenvolvimento de mapa mental para analisar o fenômeno, as variáveis e os principais aspectos que impactam cada uma delas. 


##### Passo 03 - Filtragem dos dados: Filtragem das linhas e excluir as colunas que não são relevantes para o modelo ou não fazem parte do escopo do negócio. EX: Dias em que as lojas estavam fevhadas ou inoperantes.


##### Passo 04 - Análise Exploratória dos dados: Exploração dos dados para encontrar insights.


##### Passo 05 - Preparação dos dados: Preparação para as aplicações de modelos de machine learning.


##### Passo 06 - Seleção de Features: Seleção dos melhores atributos para treinar o modelo. Utilizamos o algoritmo Boruta para essa seleção.


##### Passo 07 - Modelagem de Machine Learning: Foram realizados testes e treinamentos de alguns modelos de machine learning, para possibilitar a comparação da performance e escolha do modelo ideal para o projeto. Foi utilizada a técnica de Cross Validation para garantir a performance real sobre os dados selecionados.


##### Passo 08 - Hyperparameter Fine Tunning: Análise pelo método Random Search, em cima do algoritmo escolhido XBoost, para escolha dos melhores valores de cada parâmetro do modelo.


##### Passo 09 - Tradução e interpretação de erros: Aqui entendemos a performance do modelo para comunicar ao CFO quanto em dinheiro o modelo retornará à empresa. Foram usadas as métricas: MAE (Mean Absolute Error), MAPE (Mean Absolute Percentage Error) e RMSE (Root Mean Squared Error).


##### Passo 10 - Deploy do modelo em produção: Publicação em um ambiente de nuvem. Foi escolhida a plataforma Heroku.


##### Passo 11 - Planilha Google: desenvolver uma planilha na plataforma do Google que permite ao usuário listar os novos clientes, e ao solicitar a predição, a planilha utilizará do modelo em produção e fará o ranking dos clientes através do seu resultado de "score".


## 4. Entendendo os Dados
* Dados disponibilizados pela empresa na plataforma do [KAGGLE](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction).

| VARIÁVEL  |  DEFINIÇÃO  |
| ------------------- | ------------------- |
|  Id	 |  Identificador único do cliente.|
|  Gender |  Gênero do cliente.|
|Age	| Idade do cliente.|
|Driving_License	| 0, o cliente não tem permissão para dirigir e 1, o cliente tem para dirigir ( CNH – Carteira Nacional de Habilitação ).|
|Region_Code | Código da região do cliente.|
|Previously_Insured | 0, o cliente não tem seguro de automóvel e 1, o cliente já tem seguro de automóvel.|
|Vehicle_Age | Idade do veículo.|
|Vehicle_Damage | 0, cliente nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado.|
|Annual_Premium | Quantidade que o cliente pagou à empresa pelo seguro de saúde anual.|
|Policy_Sales_Channel | Código anônimo para o canal de contato com o cliente.|
|Vintage | Número de dias que o cliente se associou à empresa através da compra do seguro de saúde.|
|Response | 0, o cliente não tem interesse e 1, o cliente tem interesse.|


## 5. Principais Insights

**Hipótese 1-** Grande parte dos clientes já possuem seguro veicular. Resposta: Falsa, o número de pessoas que possuem e não possuem seguro veicular é muito próxima (175000 possuem x 160000 não possuem)

![Hipotese 1](https://user-images.githubusercontent.com/98356094/172991420-dc8172eb-0562-481f-b5e1-3abbe4b95c72.png)


**Hipótese 2-** Donos de carros com mais de 2 anos fazem menos seguro veicular. Resposta: Verdadeira, foi constatado que quanto mais novos os carros maior a quantidade de assinaturas com seguro veicular.

![Hipotese 2](https://user-images.githubusercontent.com/98356094/172991461-08df47b4-8c6c-4c9c-a08f-ac677c0fa3fd.png)


**Hipótese 3-** Quem não possui seguro veicular é mais sucetível a adiquirir seguro veicular. Resposta: Verdadeira, a pesquisa feita entre os clientes demonstra que aqueles que não possuem seguro veicular estão mais propensos a adquirir o seguro de carro.

![Hipotese 3](https://user-images.githubusercontent.com/98356094/172991481-07f2af87-55be-4387-82b1-e244ae2b7436.png)


## 6. Performance do Modelo

Para a realização desta etapa do projeto, foram aplicados os seguintes modelos:

* KNN,
* Logistic Regression,
* Extra Trees Classifier,
* Random Forest Classifier,
* Naive Bayes Classifier,
* XGBoost Classifier.

Foi possível produzir um modelo os seguintes resultados de métricas calculadas:

Precision @K: 0.3529 (proporção de itens recomendados no conjunto top-k)
Recall @K: 0.0019 (proporção de itens relevantes encontrados nas recomendações top-k)


### Comparação da performance dos modelos


### Performance final do modelo escolhido após Hyperparameter Fine Tuning


### Comparação da performance dos modelos


### Performance final do modelo escolhido após Hyperparameter Fine Tuning


## 7. Resultado Final

Descobrimos 9.340 possíveis clientes interessados em seguros de veículos, entre os 76.220 clientes em sua base de dados. Um total de 12,25%.
O ticket médio para um seguro de saúde anual da Insurance All é: R$31.669,00.

**Alcance com 20.000 ligações:**

* Com 20.000 ligações, o que representa 15,74% do conjunto dos dados, observamos que 42,5% dos clientes interessados em adiquirir o novo produto;

* O resultado foi 2,5x melhor do que o resultado aleatório.


## - Conclusão

Foi constatado que por meio da técnica Learning to Rank e das métricas top K, foi possível alcançar o objetivo em ranquear, com prioridade, àquelas pessoas que estão mais sujeitas a se interessar pelo novo porduto (seguro veicular) que a empresa deseja em ofertar para sua base de clientes.

Dessa forma, entregamos a Insurance All uma vantagem competitiva frente aos seus concorrentes ao reduzir o custo de aquisição de clientes (CAC) e ainda aumentar o faturamento.
