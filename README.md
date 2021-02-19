# ftdpack
ftdpack is a python package that acts as an API for the SEC's Failure To Deliver data. The database is automatically update by a script on my home machine every 4 hours, although the SEC only posts data every two weeks. I do this for a few reasons, but mainly just to make sure the data is up to data within a reasonable time frame incase of any oddities in the SEC posting timeframe(which is inconsistent).

# Installation 
Use the package manager [pip] to install ftdpack. 
''' bash
pip install ftdpack
'''

# Usage
''' python
import ftdpack 
from ftdpack import failuretodeliver as ftd

connection, cursor = ftd.get_access() #this will return a mysql.connector so you can do your own mysql pulls

ftd.download_csv() #this will download the entire database to your machine. Around 1gb so be careful. 
'''
# Future
This is version 1 of this package. I plan on adding many more functions to the failuretodeliver module as well as the ftdpack. I will add functionality to download customizable subsets of the data as well as boilerplate sql pulls. 

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. If you have any suggestions please don't hesitate to reach out. 
