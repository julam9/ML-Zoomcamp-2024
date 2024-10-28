import pickle 
from flask import Flask, request, jsonify

with open('model1.bin', 'rb') as model:
    model_q4 = pickle.load(model)

# load the dict vectorizer
with open('dv.bin', 'rb') as dv:
    dv_q4 = pickle.load(dv)  

app = Flask('subscription')

@app.route('/predict_q4', methods=['POST'])
def predict():
    customer = request.get_json()
    
    X = dv_q4.transform([customer])
    y_pred = model_q4.predict_proba(X)[0, 1]
    
    result = { 
              'subscription_probability' : float(y_pred),
              }
    return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)