# Advent of code projects

## Make day scripts
The below scripts generate a new directory called "<year_you_want>/day<day_you_want>/", get the input from the advent of code website using curl (cookies needed, since inputs are different for every user), also make a "input_small.txt" file that is to be filled by the user for the example input. 

Finally, it generates a python script for each part of the day with specified boilerplate code specified in the script file. 
To generate a day for the year **2024** and **day 1**:  

For Linux:

    . ./make_day <year> <day>
    . ./make_day 2024 1

For Powershell (not updated yet):

    .\make_day_ps.ps1 <day>