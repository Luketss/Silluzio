Important, for the second file, I decided to name it legislators-bills.csv

1. Discuss your solution’s time complexity. What tradeoffs did you make?
To analyze time complexity I would start with the number of files, takes O(n) time per file, where n is the size of the file. For each record in this files we need to store them in the runtime database O(1) per record. In a scenario with more time to spend on the solution, I would implement a relational database here, it would make easier to work and understand. The way the code is design, it would be very bad if the database have millions of registers. This code contains lots of iteration through the dict database, In a case where is a very big database and I'm using a relational database, we could use a different algorithm to avoid iterating too many times through the same array spliting it in a half and checking the id. 

2. How would you change your solution to account for future columns that might be
requested, such as “Bill Voted On Date” or “Co-Sponsors”?
I design the code thinking on future improvements, so the code can be easily changed. If we need to access a new column, it is stored in a runtime database.

3. How would you change your solution if instead of receiving CSVs of data, you were given a
list of legislators or bills that you should generate a CSV for?
this question is hard to awnser, this list would be a tuple? I would have access to headers? or I just need to parse values to a CSV? If I don't have any headers, or delimitation, and all of my values come as a list, would be hard to know were should we split, where is a new row.

4. How long did you spend working on the assignment?
The code itself about 2 hours, but documentation and review took a little more, I would say 3 hours in total.

This code uses built-in libs from python, to run it, you don't need to install external libs. Make sure you have python installed in your machine and it is on environment variables (i'm using windows, as this is not a complete doc, would be good to use windows as well). With more time, I would create a docker file for this.

Use the following command to run:
```
python main.py
```