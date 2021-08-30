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
  

def get_lines_from_dict(data) -> list:
    '''
        Get all text line-by-line from the loaded data dictionary.

        Parameters:
        data (dict): loaded dictionary containing ocr data

        Returns:
        lines (list): returns a list of lines of text
    '''
    logger.info('get_lines_from_dict called')

    blocks = data['Blocks']
    lines = []  # To store all the text lines

    # Iterate over all LINE blocks only and append text line
    for block in blocks[1:]:
        if block['BlockType']=='LINE':
            lines.append(block['Text'])
        else:
            break

    return lines


'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    
    # load json data into a dictionary
    data = get_data_from_json(dirpath)
    
    # extract the lines from dictionary
    lines = get_lines_from_dict(data)
    print(lines)

    # write logic using regex to get all lines with $ or Total or Credit or Debit

    return 0.0

if __name__=='__main__':
    extract_amount('D:\\Projects\\Fyle-Internship-Challenege\\fyle-interview-de-intern\\data\\receipt2')