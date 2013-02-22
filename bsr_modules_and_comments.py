import string

def generateOutput(template,csv):
    """ Writes data to the individual files.  i starts at 1 to
        skip the heading row of the CSV.
        outputLines is used to store lines from the template to
        allow the substitutions for writing to the file.
        After storing all of the substitutions in one outputLines[i],
        a file is opened with the respective <hostname> value if
        possible, or output<row number> otherwise. Then the output
        is written to the output file and the file is closed.        
    """
    outputLines = [''] * len(csv)
    for line in template:
        for i in range(1, len(csv)):
            outputLines[i] = line
            for j in range(0, len(csv[i])):
                outputLines[i] = outputLines[i].replace(csv[0][j],csv[i][j])
            if csv[0][0] == '<hostname>' and csv[i][0] != '':
                outputFile = open(csv[i][0] + '.txt', 'a')
            else:
                outputFile = open('output' + str(i) + '.txt','a')
            outputFile.write(outputLines[i])
            outputFile.close()

def importCSV(CSVFileName):
    """ Reads in each line of CSVFile and converts the
        comma-separated data into one array per line before
        storing them in csv[] """
    csv = []
    CSVFile = open(CSVFileName,'r')
    for line in CSVFile:
        csv.append(line.rstrip('\n').split(','))
    CSVFile.close()
    return csv

def importTemplate(templateFileName):
    templateFile= open(templateFileName,'r')
    template = templateFile.readlines()
    templateFile.close()
    return template

importedCSV = importCSV('bsr.csv')
importedTemplate = importTemplate('bsr.txt')
generateOutput(importedTemplate, importedCSV)
print 'done'
