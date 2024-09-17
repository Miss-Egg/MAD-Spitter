# MAD-Spitter
Takes out outliers (multiplier * absolute deviation around the median)

This program takes your cleaned and organized data file and deducts outliers and saves a new file with the deducted outliers.
What determines an outlier is the absolute deviation around the median (multiplied by your set multiplier) per column.



I recommend reading "Detecting outliers: Do not use standard deviation around the mean, use absolute deviation around the median"
https://doi.org/10.1016/j.jesp.2013.03.013
By Leys, Ley, Klein, Bernard, and Licata.



Directions:

Save this program into the same directory as the file you want to MAD on.
Note to use a csv file and that it has to be the only csv file in it.

It will find the median aboslute deviation of each valid header.
Valid header = nothing with "subj", "subjectid", "subject", "trials" in it.

Asks user to input the desired MAD multiplier. 3 is the default if user just presses "ENTER" on the keyboard

2 Output files into a created folder
1: valid values
2: MAD info


***This program was made so that beginner programmers or non-programmers (with a brief youtube tutorial view about using a python IDE) could use.
Please feel free to edit for your own use.***
