# readline method()
f=open('myfile.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)

# writeline method()
f=open('myfile.txt','w')
line=['line 1\n','line 2\n','line 3\n']
f.writelines(line)
f.close()

# writeline method() using for loop
f=open('myfile.txt','r')
line=['line 1','line 2','line 3']
for l in line:
    f.write(l + '\n')
f.close()
