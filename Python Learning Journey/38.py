# read a file
f = open('myfile.txt', 'r')   # use .txt for clarity
text = f.read()
print(text)
f.close()

# write a file (overwrite if exists)
f = open('myfile.txt', 'w')
f.write("Hello world!\n")   # added newline
f.close()

# append in a file if already existed
f = open('myfile.txt', 'a')
f.write("This is python learner.\n")  # added newline
f.close()
