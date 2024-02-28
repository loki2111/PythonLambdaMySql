import csv
#field names
fields = ['empid', 'empname', 'empaddress']
# data rows of csv file
rows = [{
	"empid": "100",
	"empname": "vamsi",
	"empaddress": "ap"
},{
	"empid": "200",
	"empname": "krishna",
	"empaddress": "Karnataka"
}]

with open('empdata.csv', 'w', newline='') as csvfile:
	fieldnames = ['empid','empname','empaddress']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(rows)