import csv
import os

def createfiles():
    if os.path.exists("req.csv"):
        os.remove("req.csv")

    if os.path.exists("del.csv"):
        os.remove("del.csv")

    with open('req.csv', 'w+', newline='\n') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Name", "Number", "Home Address"])

    with open('del.csv', 'w+', newline='\n') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Name", "Number", "Home Address"])

def appendfile(filename, form):
    with open(filename, 'a', newline='\n') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([form.name.data, form.tel.data, form.address.data])
