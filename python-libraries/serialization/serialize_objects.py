#######################################
# Serialization of objects: Dictionary
#######################################
import pickle

# Create a Dict
Dict1={'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}

# Serialize an Dict
l_serialization_loc = "E:/Training\\PythonSep2023\\PYTHON_MODULES/serialization\\object1.pickle"
with open(l_serialization_loc, 'wb') as f:
	pickle.dump(Dict1, f)

# DeSerialize File to Object
with open(l_serialization_loc, 'rb') as f:
	DictFile = pickle.load(f)
    
print(DictFile)
