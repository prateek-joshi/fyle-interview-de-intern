# Your imports go here
import logging
import os
import json

logger = logging.getLogger(__name__)


def get_data_from_json(dirpath: str) -> dict:
    '''
        Extracts data from the json file within the specified directory into a dictionary.

        Parameters:
        dirpath (str): directory path containing receipt and ocr output

        Returns:
        data (dict): returns the extracted data as a dictionary
    '''
    # get path of json
    ocr_json_path = os.path.join(dirpath,'ocr.json')

    logger.info('get_data_from_json called for file %s', ocr_json_path)
    # load json into dictionary
    with open(ocr_json_path, 'r') as f:
        data = json.load(f)

    return data
  

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    
    data = get_data_from_json(dirpath)
    print(data['Blocks'][1]['Text'])
    # extract the lines from dictionary
    # write logic using regex to get all lines with $ or Total or Credit or Debit

    return 0.0

if __name__=='__main__':
    extract_amount('D:\\Projects\\Fyle-Internship-Challenege\\fyle-interview-de-intern\\data\\receipt1')