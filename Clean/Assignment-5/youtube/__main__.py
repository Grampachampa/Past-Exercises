"""
XB_0082: The Youtube Trending Analyzer
Author: Leon Willems

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""
# Both here, and in the tools import of the diagnostics file, i have removed the "youtube." tools of the import (ie. import youtube.tools is just import tools)
# If the code starts throwing errors, that's probably why. try changing the tools import to "import youtube.tools as tools", and if so, do the same with the diagnostics import within tools
# It wouldn't work for me any other way, and as such, I apologize for the inconvenience
import tools
import diagnostics

# Don't execute this if file is imported
if __name__ == '__main__':
    entries = tools.read_file('videos.csv')
    tools.dataset_viewer(entries)
    tools.analyzer(entries)
    
