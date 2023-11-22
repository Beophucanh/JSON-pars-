#import json class library in 
import json

#Create the data dictionary 

data = {

    'name': 'Phuc',
    'age': 21,
    'city': 'Seattle',
    'interest': ['tennis', 'classical music', 'daydreaming'],
    'is_student': True,
}

#This opens the file as json_file and writes to the file.
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')

#This allows you to open the file succesfully and able to read.
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#Modify the Json data. we add a string to append.
loaded_data['age'] = 27
loaded_data['interests'].append('sports')

#We modify the data back to the JSON file.
with open('data.json', 'w') as json_file:
    
    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')
