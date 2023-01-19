# Voter
This repo is comprised of two parts.
Part 1 is Voter_Pull.py. This pulls specific districts from the Ohio voter website, and stores them
in the corresponding txt files.

Through dataframe manipulation, and probabilistic search, 
the individuals in the voter_data.csv file are cross checked against all of the districts...
in this case, districts 1-4...but all 80 can be checked if necessary.

The ID that best fits the chance that their name, zip code, birth year, etc, matches up, is linked to their profile. 
Then, the new dataframe is saved back to CSV.

This entire process is automated through the Voter_Match.py file.
