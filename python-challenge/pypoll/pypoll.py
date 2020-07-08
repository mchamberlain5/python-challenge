#module for reading csv files
import os
import csv


#create the path for csv files
csvpath = os.path.join('resources','election_data.csv')

#open csv with read function

with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ',')
	csv_header = next(csvreader)
	

#create lists 
	county = []
	candidate= []
	candidate_unique= []
	winner= []
	total_votes = 0

##create a list of votes
	

	for row in csvreader:
		total_votes += 1
		candidate.append(row[2])
		
print(total_votes)

from collections import Counter 

#Count the votes for persons and stores in the dictionary 
vote_count=Counter(candidate) 

print(vote_count)

#Find the maximum number of votes 
max_votes=max(vote_count.values()) 

print(f"winner, {max_votes}")

#Search for people having maximum votes and store in a list 
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes] 

#Sort the list and print lexicographical smallest name 
print(sorted(lst)[0]) 

for key in vote_count:
	percentage = round(((vote_count[key])/total_votes)*100)
	
	print(f"{key}: {vote_count[key]} {percentage}%")
	



#---------------------------------------------------------------------------------



output_file = os.path.join("pypoll_results.txt")
with open(output_file, 'w') as datafile:
	

	datafile.write('Election Results')
	datafile.write(f'Total Votes: {total_votes}')
	datafile.write(f"{key}: {vote_count[key]} {percentage}%")
	datafile.write(f"winner: {sorted(lst)[0]}")