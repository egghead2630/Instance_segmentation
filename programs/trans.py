f = open('test_img_ids.json', 'r')
lines = []
for l in f:
    lines.append(l)

f.close()


f = open('test_img_ids.json', 'w')

f.write('{\n')

f.write('\"images\": ')
for line in lines:
    f.write(line)
f.write(', \n')

f.write('\"categories\": \n')

f.write('[\n')
f.write('{\"id\": 1, \"name\": 1}\n')
f.write(']\n')

f.write('}\n')
