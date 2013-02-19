import string
csv = []
f = open('bsr.csv','r')
for line in f:
    csv.append(line.rstrip('\n').split(','))
f.close()
f= open('bsr.txt','r')
template = f.readlines()
f.close()

ll = [''] * len(csv)

for l in template:
    for i in range(1, len(csv)):
        ll[i] = l
        for j in range(0, len(csv[i])):
            ll[i] = ll[i].replace(csv[0][j],csv[i][j])
        if csv[0][0] == '<hostname>' and csv[i][0] != '':
            f = open(csv[i][0] + '.txt', 'a')
        else:
            f = open('output' + str(i) + '.txt','a')
        f.write(ll[i])
        f.close()
print 'done'
