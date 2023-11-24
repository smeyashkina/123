domen_count = {}

with open('out.csv') as f:
    for line in f:
        line = line.split(',')
        for i in line:
            if i.count('@')==1:
                for j in range(len(i)):
                    if i[j]=='@':
                        b = i[j+1::]
                        break

        if b in domen_count:
            domen_count[b] += 1
        else:
            domen_count[b] = 1

print(domen_count)
domen_sorted = sorted(domen_count.items(), key=lambda item: item[1], reverse=True)
file = open('file.csv', 'w+')
a = 'domen, count' + '\n'
file.write(a)
for i in domen_sorted:
    a = str(i[0]) + ', ' + str(i[1]) + '\n'
    file.write(a)
print(file)