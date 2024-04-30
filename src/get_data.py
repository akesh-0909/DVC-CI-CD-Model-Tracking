import os 
import yaml
import pandas as pd
import argparse # used to parse the arguments from command line while run

def read_params(config_path):
    with open(config_path,'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config = read_params(config_path)
    print("config:",config['data_source']['s3_source'])


    # data_path = config['']

if __name__ == "__main__":
    args = argparse.ArgumentParser() # create the object 
    args.add_argument("--config") # fetch the arguments parsed form cmd liine
        # python src/get_data.py --config "params.yaml" or default = path.yaml
    parsed_args = args.parse_args() #  see the parsed arg which is config path here
    get_data(config_path=parsed_args.config)
    
    
''' 
python src/get_data.py --config "params.yaml"

config: {'base': {'project': 'winequality-project', 'random_state': 42, 'target_col': 'TARGET'}, 'data_source': {'s3_source': 'data_given/winequality.csv'}, 'load_data': {'raw_dataset_csv': 'data/raw/winequality.csv'}, 'split_data': {'train_path': 'data/processed/train_winequality.csv', 'test_path': 'data/processed/test_winequality.csv', 'test_size': 0.2}, 'estimators': {'ElasticNet': {'params': {'alpha': 0.88, 'l1_ratio': 0.89}}}, 'model_dir': 'saved_models', 'reports': {'params': 'report/params.json', 'scores': 'report/scores.json'}, 'webapp_model_dir': 'prediction_service/model/model.joblib'}
(development) PS D:\my work\mlops by sunny> python src/get_data.py --config "params.yaml"


python src/get_data.py --config "params.yaml"

config['base']
config: {'project': 'winequality-project', 'random_state': 42, 'target_col': 'TARGET'}
(development) PS D:\my work\mlops by sunny> 
'''