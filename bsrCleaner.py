import string

# Load the CSV
csv = []
f = open('bsr.csv','r')
for line in f:
    csv.append(line.rstrip('\n').split(','))
f.close()

# Load the template
f= open('bsr.txt','r')
template = f.readlines()
f.close()

# Initialize line_output array
line_output = [''] * len(csv)


for line in template:
    # Skip header row of CSV
    for i in range(1, len(csv)):
        # Store line so that it can be edited
        line_output[i] = line
        # Perform substitutions
        for j in range(0, len(csv[i])):
            line_output[i] = line_output[i].replace(csv[0][j],csv[i][j])
        # Name file based on the <hostname> value
        if csv[0][0] == '<hostname>' and csv[i][0] != '':
            f = open(csv[i][0] + '.txt', 'a')
        # Otherwise name it output<row number>.txt
        else:
            f = open('output' + str(i) + '.txt','a')
        f.write(line_output[i])
        f.close()
print 'done'
