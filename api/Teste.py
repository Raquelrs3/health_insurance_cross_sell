import os
import pickle
import pandas as pd
from flask             import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance 

print('inicializando')

def health_insurance_predict(dados):
    model = pickle.load( open('/Users/raquelrocha/Documents/ProjetosComunidadeDS/Health_Insurance_Cross_Sell_Prediction/model/model_health_insurance.pkl', 'rb' ) )

    test_json = dados
    print(test_json)
    if test_json: #se tem dados
        if isinstance (test_json, dict): #uma linha só se for dicionário, mais de uma linha se for json 
            test_raw = pd.DataFrame (test_json, index = [0]) #dados de teste
        
        else: #multiple example
            test_raw = pd.DataFrame (test_json, columns = test_json[0].keys()) #se houver várias linhas será dessa forma
    
        # Instantiate HealthInsurance Class
        pipeline = HealthInsurance()
    
        #data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        #feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        #data preparation
        df3 = pipeline.data_preparation(df2)
        
        #prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
    
    else:
        #return Response("{}", status = 200, minetype = "application/json")
        print('return')
json = [{"id": 148532, "gender": "Male", "age": 29, "driving_license": 1, "region_code": 28, "previously_insured": 0, "vehicle_age": "between_1_2_year", "vehicle_damage": 1, "annual_premium": 42064.0, "policy_sales_channel": 155, "vintage": 184, "response": 1}, {"id": 277241, "gender": "Male", "age": 23, "driving_license": 1, "region_code": 46, "previously_insured": 1, "vehicle_age": "below_1_year", "vehicle_damage": 0, "annual_premium": 31675.0, "policy_sales_channel": 152, "vintage": 271, "response": 0}, {"id": 280488, "gender": "Male", "age": 74, "driving_license": 1, "region_code": 50, "previously_insured": 0, "vehicle_age": "between_1_2_year", "vehicle_damage": 1, "annual_premium": 48027.0, "policy_sales_channel": 8, "vintage": 91, "response": 0}, {"id": 380830, "gender": "Male", "age": 23, "driving_license": 1, "region_code": 28, "previously_insured": 1, "vehicle_age": "below_1_year", "vehicle_damage": 1, "annual_premium": 36042.0, "policy_sales_channel": 158, "vintage": 119, "response": 0}, {"id": 224736, "gender": "Male", "age": 24, "driving_license": 1, "region_code": 3, "previously_insured": 1, "vehicle_age": "below_1_year", "vehicle_damage": 0, "annual_premium": 32568.0, "policy_sales_channel": 160, "vintage": 248, "response": 0}, {"id": 299888, "gender": "Female", "age": 44, "driving_license": 1, "region_code": 32, "previously_insured": 0, "vehicle_age": "between_1_2_year", "vehicle_damage": 1, "annual_premium": 2630.0, "policy_sales_channel": 156, "vintage": 266, "response": 0}, {"id": 188998, "gender": "Female", "age": 57, "driving_license": 1, "region_code": 28, "previously_insured": 0, "vehicle_age": "between_1_2_year", "vehicle_damage": 1, "annual_premium": 22630.0, "policy_sales_channel": 13, "vintage": 120, "response": 0}, {"id": 52236, "gender": "Male", "age": 45, "driving_license": 1, "region_code": 28, "previously_insured": 0, "vehicle_age": "over_2_years", "vehicle_damage": 1, "annual_premium": 37782.0, "policy_sales_channel": 26, "vintage": 42, "response": 0}, {"id": 135106, "gender": "Male", "age": 24, "driving_license": 1, "region_code": 41, "previously_insured": 1, "vehicle_age": "below_1_year", "vehicle_damage": 0, "annual_premium": 95165.0, "policy_sales_channel": 152, "vintage": 84, "response": 0}, {"id": 277031, "gender": "Female", "age": 38, "driving_license": 1, "region_code": 3, "previously_insured": 1, "vehicle_age": "between_1_2_year", "vehicle_damage": 0, "annual_premium": 24702.0, "policy_sales_channel": 124, "vintage": 147, "response": 0}]

health_insurance_predict(json)        