import pickle

# load the model
with open('model1.bin', 'rb') as model:
    model_q3 = pickle.load(model)

# load the dict vectorizer
with open('dv.bin', 'rb') as dv:
    dv_q3 = pickle.load(dv) 

data_q3 = {"job": "management", 
           "duration": 400, 
           "poutcome": "success"}

X_q3 = dv_q3.transform([data_q3])
y_pred_q3 = model_q3.predict_proba(X_q3)[0, 1]

print('input:', data_q3)
print('output:', y_pred_q3)