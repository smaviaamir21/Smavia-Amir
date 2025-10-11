#import function
import os
#it will create data name folder
# os.mkdir("data")

if(not os.path.exists("data")):
    os.mkdir("data")

# create 100 day name files in data name folder
for i in range(0,100):
    os.mkdir(f"data/day{i+1}")

#this will rename all 100 files
# for i in range(0,100):
#     os.rename(f"data/day{i+1}",f"data/lecture {i+1}")
