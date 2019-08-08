import pandas as pd
import numpy as np
import pickle

from flask import Flask, url_for, request
import json

model_path = '/pickle_model.pkl'
prd_model = pickle.load(model_path)
prd_model.summary()

app = Flask(__name__)
@app.route('/predictest')
def predicttest():
    return 'predict API working'

# main predict code
@app.route('/predict_res', methods=['POST'])
def predict_res():

    if request.method == 'POST':
        text_data = pd.DataFrame(request.json)
		
        text_out = prd_model.predict(text_data)

        #Convert df t dict and the to Json
        text_out_dict = text_out.to_dict(orient='records')
        text_out_json = json.dumps(text_out_dict, ensure_ascii=False)

        return text_out_json


if __name__ == "__main__":
     app.run(host="0.0.0.0", debug=True)
