#pybank
#create file paths across any operating system
import os

#module for reading csv files
import csv

#create the path for csv files
csvpath = os.path.join('resources','budget_data.csv')

#open csv with read function

with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ',')
	# print(csvfile.read())

	csv_header = next(csvreader)



#find the total of profits/losses
	profit_total = []
	average_changes = 0
	
	greatest_profit = 0
	greatest_loss = 0
	month_total = []	
	c = []
	change = []
	total_change = []
	date = []

	for row in csvreader:
		profit_total.append(int(row[1]))
		month_total.append(len(row[0]))
		date.append(row[0])
		
	

	#print(date)

		
	#print(profit_total)

	#create a list of changes
	for i in range(1, len(profit_total)):
		c = (profit_total[i] - profit_total[i-1])
		
		change.append(c)

	#print(change)
		
	
	total_change = sum(change)

	#print (total_change)

	final_month=len(month_total)
	average_changes = total_change/(len(change))
	#print(average_changes)

	greatest_profit = max(change)
	greatest_loss = min(change)
	
	#print(greatest_profit)
	#print(greatest_loss)

	##use index method to find index of max(change)

	#print(change.index(greatest_profit)+1)
	#print(change.index(greatest_loss)+1)
	#print(date[25])
	#print(date[44])


	#-----------------------------------------------------------------------
	


final_profit=sum(profit_total)

#------------------------------------------------------------------------------------------------------------------------
#summary table
print("Financial Analysis")
print (f'Total Months: {final_month}')
print(f'Total: ${final_profit}')
print(f'Average Change: ${average_changes}')
print(f'Greatest Increase in Profits:{date[25]} ${greatest_profit}')
print(f'Greatest Decrease in Profits:{date[44]} ${greatest_loss}')


output_file = os.path.join("pybank_results.txt")
with open(output_file, 'w') as datafile:
	

	datafile.write('Financial Analysis')
	datafile.write(f'Total Months: {final_month}')
	datafile.write(f'Total: ${final_profit}')
	datafile.write(f'Average Change: ${average_changes}')
	datafile.write(f'Greatest Increase in Profits:{date[25]} ${greatest_profit}')
	datafile.write(f'Greatest Decrease in Profits:{date[44]}${greatest_loss}')