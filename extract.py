# Your imports go here
import logging
import os
import json
import re

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
    with open(ocr_json_path, 'r', encoding='utf-8') as f:
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
            lines.append(block['Text'].lower())
        else:
            break

    return lines


def extract_amount(dirpath: str) -> float:
    '''
        Given a directory with receipt file and OCR output, this function should extract the amount

        Parameters:
        dirpath (str): directory path containing receipt and ocr output

        Returns:
        float: returns the extracted amount

    '''
    logger.info('extract_amount called for dir %s', dirpath)

    # load json data into a dictionary
    data = get_data_from_json(dirpath)

    # extract the lines from dictionary
    lines = get_lines_from_dict(data)

    lines_with_amount = []
    for i in range(1,len(lines)-1):
        # if line contains $
        if re.search('$', lines[i]):
            # line contains amount and $ together
            if re.search(r'[0-9]+\.[0-9]+', lines[i]):
                lines_with_amount.append(lines[i])
            # if next line contains the amount
            elif re.search(r'[0-9]+\.[0-9]+', lines[i+1]):
                lines_with_amount.append(lines[i+1])

        elif any(ele in lines[i] for ele in ['Payment', 'Total', 'Credit', 'Debit']):
            lines_with_amount.append(lines[i+1])

    # print(lines_with_amount)
    amounts = []
    for amt in lines_with_amount:
        # get only the amount from all the lines
        a = re.search(r'([0-9]|\.|,)+',amt).group()
        # remove all ocurrences of commas
        amounts.append(float(a.replace(',','')))

    # print(amounts)

    return max(amounts)
