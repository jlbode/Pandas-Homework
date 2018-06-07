# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:17:27 2018
@author: bodej
Option #2: Academy of Py

"""


#1. Read in libraries
import pandas as pd
import numpy as np
import os

#2. Read in Data
path_schools = os.path.join("raw_data", "schools_complete.csv") 
path_students = os.path.join("raw_data", "students_complete.csv") 
schools = pd.read_csv(path_schools) 
students = pd.read_csv(path_students) 

#3. Print out Head of datasets
print(schools.head())
print(students.head())


#4. DISTRICT SUMMARY

#Produce the metrics
totschools = schools['School ID'].count()
totstudents = students['Student ID'].count()
totbudget = schools["budget"].sum()
avgmath = students["math_score"].mean()
avgreading = students["reading_score"].mean()
#students["Pass Math"] = students.loc[[:, students['math_score']>=60]]
#pctpass_math = students["Pass Math"].mean()
#pctpass_reading = 

#Create a Data Frame from the Metrics

#Show results
summary = {
    "Total Schools" : totschools , 
    "Total Students" : totstudents , 
    "Total Budget" : totbudget , 
    "Average Math Score" : avgmath , 
    "Average Reading Score" : avgreading 
}

df_summary = pd.DataFrame(data = summary, index = [0])
print(df_summary.T)

summary


"""
data = pd.read_json(file, orient = 'records')

## Option 2: Academy of Py
### District Summary

* Create a high level snapshot (in table form) of the district's 
key metrics, including:
  * Total Schools
  * Total Students
  * Total Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### School Summary

* Create an overview table that summarizes key metrics about each school, including:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Top Performing Schools (By Passing Rate)

* Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Bottom Performing Schools (By Passing Rate)

* Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.

### Math Scores by Grade**

* Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

### Reading Scores by Grade

* Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

### Scores by School Spending

* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)

### Scores by School Size

* Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).

### Scores by School Type

* Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).

As final considerations:

* Your script must work for both data-sets given.
* You must use the Pandas Library and the Jupyter Notebook.
* You must submit a link to your Jupyter Notebook with the viewable Data Frames.
* You must include an exported markdown version of your Notebook called  `README.md` in your GitHub repository.
* You must include a written description of three observable trends based on the data.
* See [Example Solution](PyCitySchools/PyCitySchools_Example.ipynb) for a reference on the expected format.

## Hints and Considerations

* These are challenging activities for a number of reasons. For one, these activities will require you to analyze thousands of records. Hacking through the data to look for obvious trends in Excel is just not a feasible option. The size of the data may seem daunting, but Python Pandas will allow you to efficiently parse through it.

* Second, these activities will also challenge you by requiring you to learn on your feet. Don't fool yourself into thinking: "I need to study Pandas more closely before diving in." Get the basic gist of the library and then _immediately_ get to work. When facing a daunting task, it's easy to think: "I'm just not ready to tackle it yet." But that's the surest way to never succeed. Learning to program requires one to constantly tinker, experiment, and learn on the fly. You are doing exactly the _right_ thing, if you find yourself constantly practicing Google-Fu and diving into documentation. There is just no way (or reason) to try and memorize it all. Online references are available for you to use when you need them. So use them!

* Take each of these tasks one at a time. Begin your work, answering the basic questions: "How do I import the data?" "How do I convert the data into a DataFrame?" "How do I build the first table?" Don't get intimidated by the number of asks. Many of them are repetitive in nature with just a few tweaks. Be persistent and creative!

* Expect these exercises to take time! Don't get discouraged if you find yourself spending  hours initially with little progress. Force yourself to deal with the discomfort of not knowing and forge ahead. This exercise is likely to take between 15-30 hours of your time. Consider these hours an investment in your future!

* As always, feel encouraged to work in groups and get help from your TAs and Instructor. Just remember, true success comes from mastery and _not_ a completed homework assignment. So challenge yourself to truly succeed!

## Copyright

Trilogy Education Services (C) 2018. All Rights Reserved.

"""