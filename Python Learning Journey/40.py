# seek() function
with open('myfile.txt','r') as f:
    f.seek(10)
    print(f.read(5))
    f.close()

#tell() function   
with open('myfile.txt','r') as f:
    print(f.read(10))
    current_position=f.tell()
    print(f.seek(current_position))
    f.close()

#truncate() function
with open('myfile.txt','w') as f:
    f.write('Hello World!')
    f.truncate(12)
    f.close()

with open('myfile.txt','r') as f:
    print(f.read())
    f.close()
