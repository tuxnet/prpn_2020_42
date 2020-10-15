# myfile = open('dirlist.txt')
# print(type(myfile))
# content = myfile.readlines()
# print(type(content))
# print(content)
# for item in content:
#     print(item)
# myfile.close()
# myfile = open('dirlist.txt')
# print(myfile.readline())
# print(myfile.readline())
# myfile.close()
myfile = open('dirlist.txt')
outfile = open('newdirlist.txt', 'w') # ('r','w','a', 'x')
for line in myfile:
    if '.java' in line:
        outfile.write(line.replace('.java', '.py'))
myfile.close()
outfile.close()
# with open('dirlist.txt') as f:
#     print(f.readlines())
# print(f.closed)
