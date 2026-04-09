# 4. Pattern Recognition & String Processing
# Project Title Formatter
# Problem: Student project titles submitted online are inconsistently formatted. A valid formatted title must:

# Be between 5 and 50 characters long
# Contain no leading or trailing whitespace
# Have every word capitalized (title case)
# Contain no special characters except hyphens and apostrophes

# Input: A list of raw project title strings
# Output:
# For each title: either the correctly formatted version, or "INVALID" if it cannot be made valid (e.g., wrong length after stripping)
# Skills tested: String methods, regex or character inspection, transformation logic

import re
import string

list_of_titles = ["Adaptation of desert tortoises to water shortages ",
                  "  Space: a cool place to Be",
                  "Help",
                  "THis is a really long TITLE that I dont know what else to say and im going to submit it and get an F!!",
                  "A Nice Title That Sould Be Formatted Correctly",
                  "My Project - Some stuff I made for friend's"]

def check_title(title):
    stripped_title = title.strip()
    # first rule
    if not 5<=len(stripped_title)<=50:
        return "INVALID"
    # remove special characters
    modified_title = re.sub(pattern=r"[^a-zA-Z0-9'\- ]", repl='', string=stripped_title)
    modified_title = string.capwords(modified_title)
    return modified_title


for title in list_of_titles:
    print(check_title(title=title))




