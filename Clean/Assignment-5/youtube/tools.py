"""
XB_0082: The Youtube Trending Analyzer
Author: Leon Willems

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

import csv
from typing import List
from inspect import getmembers, isfunction
import diagnostics as diagnostics
from pathlib import Path


def read_file(file_name: str = None) -> List[List]:
    """
    Reads in a given file, entered by the user, containing Youtube
    trending video data. These data are outputted to a List[List]
    construction, e.g. a list with all videos.
    :param file_name: the file name, for testing purposes
    :return: all videos in a list
    """
    path = Path(__file__).parent / f'../data/{file_name}'
    entries = []

    print('Reading dataset...')
    with open(path, 'r', encoding='utf8') as csvfile:
        video_reader = csv.reader(csvfile)
        for row in video_reader:
            entries.append(row)

    return entries


def dataset_viewer(entries: List[List]) -> None:
    """
    Prints the first line of data, for data understanding purposes.
    :param entries: all video data in a list
    :return: nothing, prints video data
    """
    print("The column positions, column names and value examples of this dataset look as follows:")
    for i in range(len(entries[0])):
        print(f'[{i}] {entries[0][i]}: {entries[1][i]}')
    print()

    return


def analyzer(entries: List[List]) -> None:
    """
    Function to ask the user what they would like to analyze.
    :param entries: all video data in a list
    :return: nothing, outputs the desired results according
    to the function that is called
    """
    print('Hello, welcome to the Youtube Trending Analyzer')

    # Checks what functions exist in diagnostics.py
    functions = getmembers(diagnostics, isfunction)
    print('Currently, we have the following functions:')
    for idx, func in enumerate(functions):
        print(f'[{idx}] {func[0]}')

    # Lets the user decide what analysis to run
    number = input('What would you like to know? ')
    print()

    # Runs the analysis
    obtained_function = getattr(diagnostics, functions[int(number)][0])
    obtained_function(entries)