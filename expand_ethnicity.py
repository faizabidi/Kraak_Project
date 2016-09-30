#!/usr/bin/python
import csv

# Open the CSV file
inp = raw_input ("Enter file name: ")

try:
    if len(inp) < 1:
        inp = "AllData.csv"
    file = open(inp)
except:
    print("File not found")
    exit(1)

# Read the CSV file
csv_file = csv.reader(file)
output_file = csv.writer(open(
    "/Users/faizabidi/git/Kraak_Project/appended_file.csv", 'w'))
ethnicity = list()
for row in csv_file:
    ethnicity.append(row[6])

    if row[6] == "WFO":
        row[8] = "White"
        row[9] = "Female"
        row[10] = "Other"

    elif row[6] == "WFA":
        row[8] = "White"
        row[9] = "Female"
        row[10] = "Athlete"

    elif row[6] == "WFE":
        row[8] = "White"
        row[9] = "Female"
        row[10] = "Entertainer"

    elif row[6] == "LFE":
        row[8] = "Latina"
        row[9] = "Female"
        row[10] = "Entertainer"

    elif row[6] == "MFA":
        row[8] = "Mixed"
        row[9] = "Female"
        row[10] = "Athlete"

    elif row[6] == "BMA":
        row[8] = "Black"
        row[9] = "Male"
        row[10] = "Athlete"

    elif row[6] == "LFA":
        row[8] = "Latina"
        row[9] = "Female"
        row[10] = "Athlete"

    elif row[6] == "MFE":
        row[8] = "Mixed"
        row[9] = "Female"
        row[10] = "Entertainer"

    elif row[6] == "AMO":
        row[8] = "Asian"
        row[9] = "Male"
        row[10] = "Other"

    elif row[6] == "BME":
        row[8] = "Black"
        row[9] = "Male"
        row[10] = "Entertainer"

    elif row[6] == "AMA":
        row[8] = "Asian"
        row[9] = "Male"
        row[10] = "Athlete"

    elif row[6] == "LFO":
        row[8] = "Latina"
        row[9] = "Female"
        row[10] = "Other"

    elif row[6] == "AME":
        row[8] = "Asian"
        row[9] = "Male"
        row[10] = "Entertainer"

    elif row[6] == "BMO":
        row[8] = "Black"
        row[9] = "Male"
        row[10] = "Other"

    elif row[6] == "BFA":
        row[8] = "Black"
        row[9] = "Female"
        row[10] = "Athlete"

    elif row[6] == "AFO":
        row[8] = "Asian"
        row[9] = "Female"
        row[10] = "Other"

    elif row[6] == "BMA ":
        row[8] = "Black"
        row[9] = "Male"
        row[10] = "Athlete"

    elif row[6] == "BFE":
        row[8] = "Black"
        row[9] = "Female"
        row[10] = "Entertainer"

    elif row[6] == "AFE":
        row[8] = "Asian"
        row[9] = "Female"
        row[10] = "Entertainer"

    elif row[6] == "BFO":
        row[8] = "Black"
        row[9] = "Female"
        row[10] = "Other"

    elif row[6] == "AFA":
        row[8] = "Asian"
        row[9] = "Female"
        row[10] = "Athlete"

    elif row[6] == "WMO":
        row[8] = "White"
        row[9] = "Male"
        row[10] = "Other"

    elif row[6] == "WMA":
        row[8] = "White"
        row[9] = "Male"
        row[10] = "Athlete"

    elif row[6] == "WME":
        row[8] = "White"
        row[9] = "Male"
        row[10] = "Entertainer"

    elif row[6] == "MME":
        row[8] = "Mixed"
        row[9] = "Male"
        row[10] = "Entertainer"

    elif row[6] == "LMA":
        row[8] = "Latina"
        row[9] = "Male"
        row[10] = "Athlete"

    elif row[6] == "MMA":
        row[8] = "Mixed"
        row[9] = "Male"
        row[10] = "Athlete"

    elif row[6] == "LME":
        row[8] = "Latina"
        row[9] = "Male"
        row[10] = "Entertainer"

    output_file.writerow(row)

#print len(set(ethnicity))
