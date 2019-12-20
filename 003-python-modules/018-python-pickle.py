# Title: Python Pickle Serialization

# Notes:
# Serialization is the process of converting an object state 
# into a string format file or memory buffer,
# In order to resurrected for later use for a later use or 
# transmitted across a network

# serializing an object is also known as deflating or marshalling
# deserialization a string or file into an object also known as inflating or unmarshalling




import pickle;

#############################
# Serialization of an Object
#############################

# Create a Class
class PickleTest():
    
    a=0
    b=0
    
    def __init__(self,i_a,i_b):
        self.a=i_a
        self.b=i_b


# Create an Object
Obj1 = PickleTest(1,2)

# Serialize an Object
with open('object.pickle', 'wb') as f:
	pickle.dump(Obj1, f)
    
# DeSerialize File to Object
with open('object.pickle', 'rb') as f:
	ObjFile = pickle.load(f)

print(ObjFile)

print(ObjFile.a)
print(ObjFile.b)


################################
# Serialization of a Dictionary
################################
   
# Create a Dict
Dict1={'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}

# Serialize an Dict
with open('dict.pickle', 'wb') as f:
	pickle.dump(Dict1, f)

# DeSerialize File to Object
with open('dict.pickle', 'rb') as f:
	DictFile = pickle.load(f)
    
print(DictFile)


    
