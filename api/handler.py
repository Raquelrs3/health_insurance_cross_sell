import os
import pickle
import pandas as pd
from flask             import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance 

# Loading 

#Ver como vai ficar o caminho (tem que fazer isso aqui ainda)
path = '/Users/raquelrocha/Documents/ProjetosComunidadeDS/Health_Insurance_Cross_Sell_Prediction'
model = pickle.load( open('/Users/raquelrocha/Documents/ProjetosComunidadeDS/Health_Insurance_Cross_Sell_Prediction/model/model_health_insurance.pkl', 'rb' ) )
#model = pickle.load(open("/Users/raquelrocha/Documents/ProjetosComunidadeDS/DSProducao/model/model_rossmann2.pkl","rb"))

# Initialize API
app = Flask(__name__)

@app.route("/predict", methods = ["POST"]) # pode ser Post(recebe metodos que envia algum dado para receber) ou Get( pede alguma coisa)
def health_insurance_predict():
    test_json = request.get_json()
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
        return Response("{}", status = 200, minetype = "application/json")
    
if __name__ == "__main__":
    port = os.environ.get('PORT',5000)
    app.run(host="0.0.0.0", port=port)
    
