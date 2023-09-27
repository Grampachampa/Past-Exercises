# XB_0082 - Assignment 5 (2022-2023)

-----
* **Contributor 1**: Tim Jonatan But
* **VUnet ID number 1**: 2738575
  
**Date**: 22/11/2022
-----

## Introduction

Every minute, enough content is uploaded to Youtube for 500 hours of watching! That means that if you'd like to watch all Youtube content uploaded on one specific day, you'd be watching continuously your whole life (if you happen to reach the age of 82 and a half).

How do we deal with these amounts of data? First of all, should we care about all Youtube videos? Most of them might be a random mess. In this assignment, we'll be focusing on trending Youtube videos. What defines a trending Youtube video? There's probably a complicated algorithm for this, but it relies on the number of views, its age, and where the views are coming from (geolocation-wise).

Now we have trending videos, which is still a lot of content. How do we distill this further?


## The Youtube Trending Analyzer

You are data scientists with some software engineering affinity, and you would like to enable others to analyze Youtube trending data. You will be building a tool that helps others obtain some fruitful statistics and insights from a bunch of data–via simple command-line answerable questions. Don't worry, we will explain this later!

The project has already started. We are asking you to fill in the gaps and throw in your creativity to develop a new analysis.

This assignment is a low-key introduction to pair-programming using PyCharm, and Python projects. There will be some instructions while you enjoy a cup of coffee, so no need to worry yet about all these new concepts!

### Dataset
The dataset consists of daily trending videos in Great Britain (up to 200 a day). You can find all the information on Kaggle, a famous website containing many datasets, challenging tasks, and tons of inspiration from other coders. For more information visit [this link](https://www.kaggle.com/datasnaek/youtube-new/data?select=GBvideos.csv).

Please note that our project only contains the `GBvideos.csv` file, but it has been renamed as `videos.csv`. Check out the website to find out what the data looks like! The dataset is stored as a CSV file, whose values are separated by commas. The first line of the CSV file contains the following headers:

| Column | Description | 
|:-------|:------------|
| `video_id` | Video ID |
| `trending_date` | Trending date |
| `title` | Video title |
| `channel_title` | Channel title |
| `category_id` | Category ID | 
| `publish_time` | Video publish time |
| `tags` | Tags associated with the video |
| `views` | Number of views |
| `likes` | Number of likes |
| `dislikes` | Number of dislikes |
| `comment_count` | Number of comments |
| `thumbnail_link` | Link to the video thumbnail |
| `comments_disabled` | Flag that indicates if comments have been disabled |
| `ratings_disabled` | Flag that indicates if ratings have been disabled |
| `video_error_or_removed` | Flag that indicates if there is an error with the video |
| `description` | Video description |


### Getting Started
It's time to properly set up your project:
1. Install PyCharm or VSCode
2. Make sure you can run `__main__.py` (instructions found in python-interpreter.md)
3. Take a look at all the files in your project. What even are `*.py` files and how do they interact?

## Grading

This assignment consists of 3 tasks. Each task accounts for a different percentage of the grade. The correct development of each task is automatically checked by a set of unit tests. The assignment will eventually be graded by a tutor. 

Make sure all functions have type hints and a docstring that describes their purpose. You must follow all coding conventions defined on the Python Coding Standard document available via Canvas, otherwise, points will be deducted from your grade.


## Tasks
To start with the assignment, fill in the information related to the contributors' name, ID, and date, displayed at the beginning of this document:

```python
* Contributor 1: ...
* VUnet ID number 1: ...
* Contributor 2: ...
* VUnet ID number 2: ...
* Date: ...
```

Afterwards, you can focus on the development of the project.
To complete the program you will need to complete three tasks.
Each task must be developed within the **marker lines**:

```python
#// BEGIN_TODO [task_x] Title of task x

# // Extra explanation for task x
# // Maybe some hints

Here you should work on your code

#// END_TODO [task_x]
```


### Task 1: Total Views per Day (30%)

We want to know how many views the trending videos obtained in total–per day. To do so, go to the `total_views_per_day()` function in the `diagnostics.py` module. The function gets a list of videos. Each video is represented by a list, and each item in the list represents a characteristic of the video. The following table shows which property is represented at each index.

| Index | Property |
|:-----:|----------|
| 0  | Video ID |
| 1  | Trending date |
| 2  | Video title |
| 3  | Channel title |
| 4  | Category ID |
| 5  | Publish time |
| 6  | Tags |
| 7  | Views |
| 8  | Likes |
| 9  | Dislikes |
| 10 | Number of comments |
| 11 | Thumbnail link |
| 12 | Comments disabled |
| 13 | Ratings disabled | 
| 14 | Video error or video removed |
| 15 | Description |

You need to populate the `view_counter` dictionary. The keys of this dictionary are the trending dates in the data (string), and each value is the sum of views of all trending videos for that date.

**Note:** Assume that the trending dates are clean and you do not need to format them–you can use them directly as keys.


### Task 2: The Most Popular Video (35%)
In this task, you will need to implement a function that finds the most popular video. For that, create a new function in `diagnostics.py` called `most_popular`. The question is: how do we define the most popular video? Your function will need to support three different options:

1. The video with the highest number of views.
2. The video with the most likes and at least dislikes represented by $likes-dislikes$
3. the video with the best like ratio calculated as $likes \over likes+dislike$

The user should specify which of the options they want to use when calling the function similarly to the other functions in `diagnostics.py`.

The function should print the title of the found video.

Your function will automatically be picked up by the program, and thus included when running the software!

**Note:** Look carefully at how the input parameters are constructed for the other functions. You will need to define at least the `entries` parameter (`List[List]`).

**example output**
```
In the selected category the most popular video was: learn python in 10 minutes!
```

### Task 3: Controversial Videos (35%)
A video is controversial if it's like ratio is close to `0.5`. We are curious if disabling comments is more common for controversial videos. Write a function called `controversial_videos` that compares the following information between videos that enable comments and videos that have comments disabled.

1. The average like ratio.
2. The maximum like ratio.
3. The minimum like ratio.  

Make sure you print the output in a table.

**example output**
```
--------------------------------
comments enabled | true | false 
-------------------------------- 
average          | 0.5  | 0.5
--------------------------------
maximum          | 0.5  | 0.5
--------------------------------
minimum          | 0.5  | 0.5
--------------------------------

```

**Note** The like ratio is defined as $likes \over likes+dislike$

---


&copy; 2020-2022 - **TU/e** - **VU Amsterdam**