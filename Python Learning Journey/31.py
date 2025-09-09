#dictionary methods
#update method
employes1={ 122:45 , 123:89 , 125:68 , 127: 69 }
employes2={129:99, 121: 34}
employes1.update(employes2)
print(employes1)

#clear method
employes1={ 122:45 , 123:89 , 125:68 , 127: 69 }
employes1.clear()
print(employes1) # give empty dictionary

#pop() method
employes1={ 122:45 , 123:89 , 125:68 , 127: 69 }
employes1.pop(123) # removes perticuler item
print(employes1) 

#popitem() method
employes1={ 122:45 , 123:89 , 125:68 , 127: 69 }
employes1.popitem() # removes last item from the dictionary
print(employes1) 

#del method
employes1={ 122:45 , 123:89 , 125:68 , 127: 69 }
del employes1[123] # delete perticuler item
print(employes1) 
# del employes1()  # it will delete the whole dictionary
# print(employes1[122])   # it will generate error 

