import csv
# fields names
fields = ['empid','empname','empaddress']
# data rows of csv file
rows = [['100', 'vamsi', 'AP'],['200', 'krishna', 'karnataka']]
with open('employee.csv', 'w', newline='') as csvfile:
	empwriter = csv.writer(csvfile)
	# writing the fields
	empwriter.writerow(fields)
	#writing the data rows
	empwriter.writerows(rows)