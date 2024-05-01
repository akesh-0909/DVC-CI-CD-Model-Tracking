import yaml
import os
import json
import joblib
import numpy as np

params_path = 'params.yaml'
schema_path = os.path.join('prediction_service','schema_in.json')

class NotInRange(Exception):
    def __init__(self,message = "Values Entered are not in Range"):
        self.message  = message
        super().__init__(self.message)

class NotInCols(Exception):
    def __init__ (self, message = 'Not in columns'):
        self.message  = message
        super().__init__(self.message)

def read_params(config_path = params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config['webapp_model_dir']
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]
    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected Results"

def get_schema(schema_path = schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(dict_request):
    print('validating input')
    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCols
        
    def _validate_values(col,val):
        schema = get_schema()

        if not (schema[col]["min"] <= float(dict_request[col]) <= schema[col]["max"]) :
            raise NotInRange

    for col, val in dict_request.items():
        _validate_cols(col)
        _validate_values(col,val)

    return True


def form_response(dict_request):
    print('enter in form response')
    if validate_input(dict_request):
        try:
            print('validating input')
            print('this id dict reqrets',str(dict_request))
            data = dict_request.values()
            print('this is data',data)
            data = [list(map(float,data))]
            print('maped form values to data')
            response = predict(data)
            return response 
        except Exception as e:
            print('this is error line 77',str(e))
            pass
def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.values())])
            response = predict(data)
            response = {'response':response}
            return response

    except NotInRange as e:
        response = {"the_exected_range": get_schema(), "response": str(e) }
        return response

    except NotInCols as e:
        response = {"the_exected_cols": get_schema().keys(), "response": str(e) }
        return response


    except Exception as e:
        response = {"response": str(e) }
        return response


