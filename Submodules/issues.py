""" 
Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Performs all operations related to issues, which can be called from any other function

    Details: Lists and controls all operations for analyzing issues, such as the amount of open/closed issues and total issues

"""


import os
import sys
from Submodules.token_file import *

#getIssuesByType can be slow depending on the amount of issues. Look into another way of doing this. Type can be either 'closed', 'open', or 'all'
def getIssuesByType(url, type):
    count = 0                                                  #Count used to count the type of issues being found
    try:
        repo = token.get_repo(url.split("github.com/", 1)[1])      #Obtains the name identifier from the provided url, and obtains that repo from the REST API
        issuesAndPull = repo.get_issues(state=type)            #Get the issues and pull requests depending on the provided state
        for issue in issuesAndPull:
            if not issue.pull_request:                         #Sort out the Pull Requests from the issues. For some reason PyGitHub combines the two
                count = count + 1
    except:
        print("Error, invalid GitHub link")                    #Except case for potential invalid github links
        
    return count
    
"""This below can be used for testing. Comment when not being used, or delete when finishing project
url = sys.argv[1]
count = getIssuesByType(url, 'closed')
print(count)
"""