from flask import Flask, render_template,request,jsonify
import os
import yaml
import joblib
import numpy as np
from flask import render_template,Flask,request,jsonify

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root,'static')
template_dir = os.path.join(webapp_root,'templates')

app = Flask(
    __name__,
    static_folder=static_dir,
    template_folder=template_dir
         )

def read_params(config_path) :
    with open(config_path,'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config['webapp_model_dir']
    print('model dir path',model_dir_path)
    model = joblib.load(model_dir_path)
    print("this is model",model)
    prediction  = model.predict(data)
    print('this is predi',prediction)
    return prediction[0]

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {'response':response}
        print("this is response",response)
        return response 
    
    except Exception as e:
        print(e)
        error = {'error': "Something Went wrong! Try again"}
        return error    
    




@app.route('/',methods=['GET',"POST"])
def index():
    if request.method == 'POST':
        print('post req')
        try:
            if request.form:
                print('request',request.form)
                data = dict(request.form).values()
                data = [list(map(float,data))]
                print('data',data)
                response = predict(data)
                print("this is responseee",response)
                return render_template('index.html',response = response)

            elif request.json:
                response = api_response(request)
                print("response line 68",response)
                return jsonify(response)
        except Exception as e:
            print(e)
            error = {'error':"Something went wrong try again"}
            return error
        
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5000,debug = True)