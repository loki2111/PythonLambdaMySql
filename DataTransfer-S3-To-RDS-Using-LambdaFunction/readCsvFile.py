import csv
# To print data in term of Dictionary
outputlist=[]
with open('empdata.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		## To read all rows or column in key:value pair
		print(row)
		## To read specific row where you will read only values based on row sequence.
		print(row['empid'], row['empname'], row['empaddress'])
		outputlist.append(row.values())
	#printing records in dict format
	print(outputlist)