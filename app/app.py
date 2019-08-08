import pandas as pd
import numpy as np
import pickle

from flask import Flask, url_for, request, render_template
import json

model_path = '/pickle_model.pkl'
with open(model_path, 'rb') as file:
        prd_model = pickle.load(file)

app = Flask(__name__)
@app.route("/")
def predicttest():
	return """
  <h1>Jenkins Test-v3 in Docker!</h1>
  <p>It is a Jenkins CD Test...BOOOOOMMMM</p>
  """

# main predict code
@app.route("/test", methods=['POST'])
def predict_res():

    if request.method == 'POST':
        print(request.json)
	#text_data = pd.DataFrame(request.json)
	text_data = pd.DataFrame(request.json)
	print(text_data)
		
        text_out = prd_model.predict(text_data)

        #Convert df t dict and the to Json
        #text_out_dict = text_out.to_dict(orient='records')
        text_out_json = json.dumps(str(text_out), ensure_ascii=False)
	return render_template("index.html",prediction=text_out_json)

        #return text_out_json


if __name__ == "__main__":
     app.run(host="0.0.0.0", debug=True)
