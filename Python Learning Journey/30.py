#dictionaries in python
dic={ 
    # word meanings
    "Ali": "Human being",
    "Spoon": "Utensil",
    "Plant": "Living thing",
    #ID/employ
    23:"Taha",
    27:"Ahmad",
    33:"Laiba",
    45:"Amna"
}
print(dic["Spoon"])
print(dic[45])

info={'name':'Smavia', 'age':19 ,'eligible':True}
print(info)
print(info["name"]) #it can generate error if the key is not present in the dictionary
print(info.get('name')) # it will not generate error if the key not in dic and give output "none" 

print(info.keys())     # accessing keys of dic
print(info.values())   # accessing values of keys

for k in info.keys():  
    print(info[k])

for k in info.keys():
    print(f"The value corresponding to the key {k} is {info[k]}")

print(info.items())  # accessing keys and values both from the dictionary

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

