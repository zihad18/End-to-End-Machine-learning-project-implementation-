from us_visa.logger import logging
from us_visa.exception import USvisaException
from us_visa.utils import save_numpy_array_data
import sys
import numpy as np
try:
    logging.info("We are trying to save a numpy array")
    array = np.array([1,2,3,4,5])
    file_path = "array.npy"
    save_numpy_array_data(file_path=file_path, array=array)
    logging.info("We have saved the numpy array")
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys)
    




# try:
#     r = 1/0
#     print(r)
# except Exception as e:
#     logging.info(e)
#     raise USvisaException(e, sys)