import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(' ','_') for col in df.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path,sep=',',header=new_cols)
    
if __name__ == "__main__":
    args = argparse.ArgumentParser() # create the object 
    args.add_argument("--config") # fetch the arguments parsed form cmd liine
        # python src/get_data.py --config "params.yaml" or default = path.yaml
    parsed_args = args.parse_args() #  see the parsed arg which is config path here
    load_and_save(config_path=parsed_args.config)
    