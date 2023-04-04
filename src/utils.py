import os
import sys
sys.path.append('D:/vishal gotmare/ML_Project1/src/')
import pandas as pd
import numpy as np
import dill
from exceptions import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)
