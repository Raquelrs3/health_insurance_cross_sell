import pickle
import numpy  as np
import pandas as pd
import inflection

class HealthInsurance(object): #por padrão se escreve em termo case
    def __init__(self): #construtor e nos parenteses os ponteiros da classe, para acessar a classe
        self.home_path = '/Users/raquelrocha/Documents/ProjetosComunidadeDS/Health_Insurance_Cross_Sell_Prediction/' # Caminho para onde o modelo está salvo, os .pkl (os caminhos dão acesso as variáveis)
        self.annual_premium_scaler = pickle.load( open( self.home_path + 'features/annual_premium_scaler.pkl', 'rb' ) ) #caminhos para os pickle (que são as transformações)
        self.age_scaler = pickle.load( open( self.home_path + 'features/age_scaler.pkl', 'rb' ) ) #caminhos para os pickle (que são as transformações)
        self.vintage_scaler = pickle.load( open( self.home_path + 'features/vintage_scaler.pkl', 'rb' ) ) #p.s. self.home_path é para concatenar
        self.target_encode_gender_scaler = pickle.load( open( self.home_path + 'features/target_encode_gender_scaler.pkl', 'rb' ) ) #caminhos para os pickle (que são as transformações)
        self.target_encode_region_code_scaler = pickle.load( open( self.home_path + 'features/target_encode_region_code_scaler.pkl', 'rb' ) ) #caminhos para os pickle (que são as transformações)
        self.fe_policy_sales_channel_scaler = pickle.load( open( self.home_path + 'features/fe_policy_sales_channel_scaler.pkl', 'rb' ) ) #caminhos para os pickle (que são as transformações)
        
        

    def data_cleaning(self,df1):
        # 1.0 Descrição dos Dados¶

        ## 1.1 Rename Columns

        cols_old = ['id', 'Gender', 'Age', 'Driving_License', 'Region_Code',
                    'Previously_Insured', 'Vehicle_Age', 'Vehicle_Damage', 'Annual_Premium',
                    'Policy_Sales_Channel', 'Vintage' ]
        #response_y
        #Colocar em letra minúscula e snakecase
        snakecase = lambda x: inflection.underscore (x)
        cols_new = list(map(snakecase, cols_old))

        #rename
        df1.columns = cols_new


        df1.columns
        
        return df1
    
    
    
    def feature_engineering(self,df2):


        ### 2.4 Feature Engineering

        #Organizando para ter apenas nomes categóricos e numéricos nas features

        #vehicle age (tirar os símbolos)
        df2["vehicle_age"] = df2["vehicle_age"].apply(lambda x: "over_2_years" if x == "> 2 Years" else "between_1_2_year" if x == "1-2 Year" else "below_1_year")

        #vehicle damage (colocar em valores 0 e 1)
        df2["vehicle_damage"] = df2["vehicle_damage"].apply(lambda x: 1 if x =="Yes" else 0)

        #Mudando nome feature Response-x
        df2 = df2.rename({'response_x': "response"}, axis = 1)

        df2.head()
        
        return df2
    

    
    def data_preparation(self,df5):

        # 5.0 Data Preparation

        ## 5.1 Standardization 
        ##### ( calcula a média e o desvio padrão)
        
        #annual_premium
        #como aqui só tem uma feature, não precisei identificar
        df5["annual_premium"] = self.annual_premium_scaler.transform(df5[["annual_premium"]].values) # o que está dentro de [[]] me passa um array (p.s aqui mudamos o nome de ss transform para o nome do pickle feito)

        #P.S.
        df5["annual_premium"].head() # me mostra a series com dataframe
        df5[["annual_premium"]].head() # me dá uma coluna
        df5[["annual_premium"]].values # me dá só o que tem dentro e me retorna um array


        ## 5.2 Rescaling
        
        #age
        df5["age"] = self.age_scaler.transform(df5[["age"]].values) #(p.s aqui mudamos o nome de mms_age transform para o nome do pickle feito)

        #vintage
        df5["vintage"] = self.vintage_scaler.transform(df5[["vintage"]].values) #(p.s aqui mudamos o nome para o nome do pickle feito)

        #aplicando o encoding

        #gender
        df5.loc[:, "gender"] = df5["gender"].map(self.target_encode_gender_scaler) #(p.s aqui mudamos o nome para o nome do pickle feito)

        #region_code
        df5.loc[:,"region_code"] = df5["region_code"].map(self.target_encode_region_code_scaler) #(p.s aqui mudamos o nome para o nome do pickle feito)

        #vehicle_age - Get_dummys
        #aqui não usamos o pickle pq usamos o pandas para fazer a transformação
        df5 = pd.get_dummies(df5, prefix="vehicle_age", columns=["vehicle_age"])

        #policy_sales_channel - Frequency Encoding
        df5.loc[:, "policy_sales_channel"] = df5["policy_sales_channel"].map(self.fe_policy_sales_channel_scaler) #(p.s aqui mudamos o nome para o nome do pickle feito)
        df5 = df5.fillna( 0 )


        # 6.0 Feature Selection

        cols_selected = ['annual_premium','vintage', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured']
        
        return df5[cols_selected]
    
    def get_prediction(self,  model, original_data, test_data):

        # model prediction
        pred = model.predict_proba(test_data)

        #Join Prediction to original_data
        original_data["score"] = pred[:,1].tolist()
        
        return original_data.to_json(orient= 'records', date_format='iso')

