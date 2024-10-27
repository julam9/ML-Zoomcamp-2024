import pickle 
from flask import Flask, request, jsonify

model_file = "model_C=1.0.bin"

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in) 

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict(customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5 
    
    result = { 
              'churn_probability' : y_pred,
              'churn' : bool(churn) 
              }
    return jsonify(result)