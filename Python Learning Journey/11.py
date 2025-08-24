# Different Functions on Strings in Python
#finding length of string
a="Smavia."
print(a)
print(len(a))
# to convert the string into uppercase
print(a.upper())
# to convert the string into lowercase
print(a.lower())
#rstrip use to remove un imporatant thing from string
print(a.rstrip("."))
# replace the string from the other
print(a.replace("Smavia", "Noor"))
#strip the selected data from string
print(a.strip("S"))
#capitilize the first letter of heading
heading="wellcome to the pyhton learning journey"
print(heading.capitalize())
# centeralize the string
heading="wellcome to the pyhton learning journey"
print(heading.center(50))
print(len(heading))
print(len(heading.center(50)))
#count the selected characters from the string
print(a.count("a"))
#check is the string ends with the selected characters
str1="Wellcome to Pakistan!!!"
print(str1.endswith("!"))
#check is the string starts with the selected characters
str1="Wellcome to Pakistan!!!"
print(str1.startswith("W"))
#find the index of selected character
str1="His name is Taha .He is an honest man."
print(str1.find("i"))
print(str1.index("Taha"))
#check is all the string is made by using a_z, A_Z or 0_9 charaters
str1="WellcometoPakistan786"
print(str1.isalnum())
#check is the string based upon alphabets only
str1="Wellcome"
print(str1.isalpha())
#check is all the alphabets in string is in lower case
str1="wellcome to pakistan."
print(str1.islower())
#check is all the alphabets in string is in upper case
str1="Wellcome to Pakistan."
print(str1.isupper())
#printable data
str1="wellcome to : \n pakistan."
print(str1.isprintable())
# check is space in the string
str1="      " # using spacebar
print(str1.isspace())
str1="   " # using Tab
print(str1.isspace())
 # check is the given string is title or not
str1="World Health Organization"
print(str1.istitle()) #true
str1="wellcome to pakistan."
print(str1.istitle()) #False
#convert all the lower case alphabets into upper case and wise virsa
str1="World Health Organization"
print(str1.swapcase())
#change the string into title
str1="Taha is a good person. He is an honest man."
print(str1.title())
