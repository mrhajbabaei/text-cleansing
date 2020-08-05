""" This program cleanse your data before feeding it to your `! """

import os
import sys
import string
import ntpath
import argparse
import numpy as np
import pandas as pd


def main(args):
    data_path = args.data_path
    input_path, input_file = ntpath.split(data_path)
    file_extension = input_file.split('.')[-1]
    data_column = args.data_column
    output_path = args.output_path if args.output_path != None else input_path

    if file_extension.lower() == 'xls':
        df = pd.read_excel(data_path)
    elif file_extension.lower() == 'csv':
        df = pd.read_csv(data_path)
    else:
        raise Exception('file type is not acceptable!')

    
    for index, row in df.iterrows():
        data = row[data_column]
        stripped_data = data.translate(str.maketrans('', '', string.punctuation))
        df.at[index, data_column] = stripped_data

    df.to_csv(os.path.join(output_path, 'cleansed_' + input_file), sep=',')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='program parameters')
    parser.add_argument('data_path', metavar='path', type=str, help='path address of data')
    parser.add_argument('data_column', type=str, help='name of you targeted data')
    parser.add_argument('--output_path', metavar='path', type=str, help='consider same as input path if not provided', default=None)
    args = parser.parse_args()
    main(args)