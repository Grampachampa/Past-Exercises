"""
XB_0082: The Youtube Trending Analyzer
Author: Leon Willems

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

import csv
from typing import List
from pathlib import Path


def find_more_than_x_views(entries: List[List], views: int = None) -> int:
    """
    Runs through the dataset and calculates the number of trending
    videos with more than a certain number of views, given by user
    :param entries: the dataset, list of videos
    :param views: threshold number of views
    :return: number of videos with more than the threshold views
    """
    if views is None:
        views = input('Views: ')
    more_than_x_views = []

    for entry in entries[1:]:  # We skip the first entry, because they are column names
        if int(entry[7]) > int(views):
            more_than_x_views.append(entry)

    print(len(more_than_x_views))

    return len(more_than_x_views)


def total_views_per_day(entries: List[List], output_file_name: str = None) -> int:
    """
    Calculates, for each day, the sum of views for all videos on
    that day, and outputs this to a CSV file.
    :param entries: the dataset, list of videos
    :param output_file_name: name of the output file (including .csv)
    :return: returns the number of days included in the file
    """
    view_counter = {}

    #// BEGIN_TODO [task_1] Total views per day
    
    # // END_TODO [task_1]

    if output_file_name is None:
        output_file_name = input('What will be the name of your output file? ')

    path = Path(__file__).parent / f'../data/{output_file_name}'
    with open(path, 'w', newline='') as csvfile:
        views_writer = csv.writer(csvfile, delimiter=',')
        for date, views in view_counter.items():
            views_writer.writerow([date, views])

    return len(view_counter)


#// BEGIN_TODO [task_2] popular videos
def most_popular(entries: List[List], popularity_type: int = None) -> None:
    
    raise NotImplementedError
    
#// END_TODO [task_2]



#// BEGIN_TODO [task_3] controversial videos

def controversial_videos(entries: List[List]) -> None:
    raise NotImplementedError

#// END_TODO [task_3]






