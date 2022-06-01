# health_insurance_cross_sell
![1140-couple-completing-insurance-application-online](https://user-images.githubusercontent.com/98356094/157327525-535220d8-4d37-4ba2-88f6-604e6ada1736.jpeg)


# Previsão de Vendas das Lojas Rossmann


Este é um projeto realizado com dados públicos disponibilizados pela empresa na plataforma do [KAGGLE](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction).


## 1. Problema de Negócio
Nosso cliente, uma Seguradora que fornece Seguro Saúde para seus clientes, têm interesse em oferecer aos seus segurados seguro de veículos. Diante disso, precisam de uma solução para prever se seus clientes do ano passado terão interesse no seguro veicular fornecido pela empresa.

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


##### Passo 01 - Descrição dos dados:


##### Passo 02 - Feature Engineering:


##### Passo 03 - Filtragem dos dados:


##### Passo 04 - Análise Exploratória dos dados:


##### Passo 05 - Preparação dos dados:


##### Passo 06 - Seleção de Features:


##### Passo 07 - Modelagem de Machine Learning:


##### Passo 08 - Hyperparameter Fine Tunning:


##### Passo 09 - Tradução e interpretação de erros:


##### Passo 10 - Deploy do modelo em produção:


##### Passo 11 - Planilha Google:


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

**Hipótese 1**


**Hipótese 2**


**Hipótese 3**


## 6. Performance do Modelo


### Comparação da performance dos modelos


### Performance final do modelo escolhido após Hyperparameter Fine Tuning


## 7. Resultado Final


## - Conclusão

