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
    # pretty simple, we go through every list in the list of lists,
    # adding each date of each video as a key (with views) if it doesn't already exist, or adding the views to the date key if it does
    # we have to remove the first value, since it is describing the values held in each of the indeces of the other lists
    for i in entries[1:]:
        if i[1] in view_counter:
            view_counter[i[1]] += int(i[7])
            continue
        view_counter[i[1]] = int(i[7])

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
    '''
    Prints a statement regarding the most popular video based on the popularity type inserted.
    :param entries: the dataset, list of videos
    :param popularity_type: based off of an input integer, decides how the function defines popularity:
    1. The video with the highest number of views.
    2. The video with the most likes and at least dislikes represented by likes-dislikes
    3. the video with the best like ratio calculated as likes \ (likes+dislikes)
    Any other integer will prompt a re-input
    '''

    # We need a popularity type. If none is defined, the user is prompted to give one
    if popularity_type not in [1,2,3]:
        popularity_type = int(input("How would you like to define popularity?\nInput one of the following 3 numbers to decide! \n1. The video with the highest number of views.\n2. The video with the most likes and at least dislikes represented by likes-dislikes\n3. the video with the best like ratio calculated as likes \ (likes+dislikes)\n"))
    while popularity_type not in [1,2,3]:
        popularity_type = int(input("Please input a value between 1 and 3!\n"))
    
    
    #Defining name of video 
    most_popular_video: str = None

    # Then, it's as simple as having an if statement per type of procedure, and writing the code inside each

    # Type 1: for each video, we see if any previous best_video has had more views than it. If not, we name it best_video.
    if popularity_type == 1:
        most_views: int = 0

        for i in entries[1:]:
            video_name: str = i[2]
            video_views: int = int(i[7])
            if video_views > most_views:
                most_views = video_views
                most_popular_video = video_name
    
    # Type 2: for each video, we see if any previous best_video has had more (likes-dislikes) than it. If not, we name it best_video
    if popularity_type == 2:
        best_likes:int = 0

        for i in entries[1:]:
            video_name: str = i[2]
            video_likes = int(i[8])
            video_dislikes = int(i[9])
            likes_minus_dislikes = video_likes - video_dislikes

            if likes_minus_dislikes > best_likes:
                most_popular_video = video_name
                best_likes = likes_minus_dislikes

    # Type 2: for each video, we see if any previous best_video has had more (likes/(likes + dislikes)) than it. If not, we name it best_video
    if popularity_type == 3:
        best_ratio:int = 0

        for i in entries[1:]:
            video_name: str = i[2]
            video_likes = int(i[8])
            video_dislikes = int(i[9])
            if video_likes + video_dislikes == 0:
                continue
            video_ratio: float = video_likes/(video_likes + video_dislikes)

            if video_ratio > best_ratio:
                most_popular_video = video_name
                best_ratio = video_ratio

    # Print statement
    output = f"In the selected category the most popular video was: {most_popular_video}!"
    print (output)
    
#// END_TODO [task_2]



#// BEGIN_TODO [task_3] controversial videos


def controversial_videos(entries: List[List]) -> None:
    '''
    Prints a table of the average, max and min like ratios of videos with comments enabled and disabled.
    :param entries: the dataset, list of videos
    '''
    # defining maxima, totals, minima, and counters for videos with and without comments
    comment_maximum: float = 0.0
    comment_total: float = 0.0
    comment_minimum: float = 1
    comment_counter: int = 0


    censored_maximum: float = 0.0
    censored_total: float = 0.0
    censored_minimum: float = 1
    censored_counter: int = 1


    for i in entries[1:]:
        # Comments enabled by default
        comments_disabled:bool = False

        # defining video likes, video dislikes, and SKIPPING THE VIDEO if the video has 0 likes and dislikes
        video_likes = int(i[8])
        video_dislikes = int(i[9])
        if video_likes + video_dislikes == 0:
            continue

        # Calculating like ratio
        video_ratio: float = video_likes/(video_likes + video_dislikes)

        # Checking if comments are enabled
        if i[12] == "True":
            comments_disabled = True
        
        # If comments disabled
        if comments_disabled:
            # Censored_total will later be divided by censored_counter to get the average ratings for censored videos
            censored_total += video_ratio
            censored_counter +=1
            if video_ratio > censored_maximum:
                censored_maximum = video_ratio
            if video_ratio < censored_minimum:
                censored_minimum = video_ratio
            continue
        
        # Comments enabled by default
        # comment_total will later be divided by comment_counter to get the average ratings for videos with comments
        comment_total += video_ratio
        comment_counter += 1
        if video_ratio > comment_maximum:
            comment_maximum = video_ratio
        if video_ratio < comment_minimum:
            comment_minimum = video_ratio

    # Calculating Comment Average
    comment_average = (comment_total/comment_counter)
    censored_average = (censored_total/censored_counter)

    # Drawing out table
    table = {
        "Average": [comment_average, censored_average],
        "Maximum": [comment_maximum, censored_maximum],
        "Minimum": [comment_minimum, censored_minimum]
    }
    print("-------------------------------------------------------------------")
    print ("| {:<19} | {:<20} | {:<18} |".format('Comments Enabled','True','False'))
    print("-------------------------------------------------------------------")
    for key, value in table.items():
        t, f = value
        print ("| {:<19} | {:<20} | {:<18} |".format(key, t, f))
        print("-------------------------------------------------------------------")






#// END_TODO [task_3]






