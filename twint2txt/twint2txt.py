from pathlib import Path
import csv
import os
import sys

def main():
    argvs = sys.argv
    if len(argvs) != 3:
        print("Usage: python3 {}'file path'".format(argvs[0]))
        exit()
    
    # open CSV file
    csv_file = open("./" + argvs[1], 'r')

    # get row
    csvList = []
    for row in csv.reader(csv_file, delimiter="\t"):
        csvList.append(row[10]) # specified row number (0 start) you want

    # remove head row
    del csvList[0]

    # make text data to write to text data
    csvText = ""
    for a in reversed(csvList):
        csvText += a
        csvText += "\n"
    
    # write text file
    writer = open("./" + argvs[2] + ".txt", "w")
    writer.writelines(csvText)
    writer.close()
    

if __name__ == "__main__":
    main()
