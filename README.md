Advent of code projects

## Make day scripts
The below scripts generate a new directory called "2024/day<day_you_want>/, get the input from the advent of code website using curl(cookies needed, since inputs are different for every user), also make a "input_small.txt" file that is to be filled by the user for the example input. 

Finally, it generates a python script for each part of the day with specified boilerplate code specified in the script file. 
To generate a day for the year 2024:  

For linux:

    . ./make_day <day_you_want>

For powershell:

    .\make_day_ps.ps1 <day_you_want>

## Script to fetch the input for a specified day:


For linux:

    . ./get_day_input <day_you_want>
