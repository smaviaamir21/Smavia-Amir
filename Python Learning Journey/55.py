# clear and clutter files from a folder
import os

files = os.listdir("data")
i=1
for file in files:
    # print all files from folder
    # print(file)
    if file.endswith(".py"):  # select the files from these
        print(file)   # print selected files
    os.rename(f"data/{file}",f"data/{i}.py")   # rename and arrange all in a sequance
    i=i+1
