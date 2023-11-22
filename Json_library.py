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

#Opening the file and Writing data to the file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')

#Reading data from a JSON file
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#To modify the laoded data, append a string to the end 
loaded_data['age'] = 27
loaded_data['interests'].append('games')

#Writing modified data back to the same file
with open('data.json', 'w') as json_file:
    
    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')
