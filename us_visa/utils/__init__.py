import os 
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging


def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    

def write_yaml_file(file_path:str, content: object, replace: bool = False) -> None:
    """
    Write a dictionary to a YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    
def load_object(file_path:str) -> object:
    """
    Load an object from a file.
    """
    logging.info(f"Entered the load_object method of utils")
    try:
        with open(file_path, "rb") as file_obj:
            object_ = dill.load(file_obj)
        logging.info(f"Exited the load_object method of utils")
        return object_

    except Exception as e:
        raise USvisaException(e, sys) from e
    
def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to a file
    file_path: str location of the file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys) from e
    

def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of the file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USvisaException(e, sys) from e
    
def save_object(file_path: str, obj: object) -> None:
    logging.info(f"Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Exited the save_object method of utils")
    except Exception as e:
        raise USvisaException(e, sys) from e
    
def drop_columns(df: DataFrame, columns: list) -> DataFrame:

    """
    drop the columns form a pandas dataframe
    df: pandas dataframe
    columns: list of columns to drop
    """	
    try:
        df = df.drop(columns=columns, axis=1)

        logging.info("Exited the drop_columns method of utils")
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e
    
