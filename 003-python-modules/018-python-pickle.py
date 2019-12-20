""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pickle Serialization and De-Serialization
MetaDescription: Python Pickle Serialization and De-Serialization
MetaKeywords: Python Pickle Serialization and De-Serialization
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-pickle-serialization
---
MARKDOWN """

""" MARKDOWN
# Python Pickle Serialization and De-Serialization
* Serialization is the process of converting an object state into a 
  binary file, this file can be stored on filesystem or transmitted across
  network. or it can be persisted(stored) and later use. 
* Serialization of an object is also known as deflating or marshalling.
* In Python we use the **PICKLE** module to Serialize an Object.
* In order to resurrect an Object from a Pickle file it needs to be deserialized
* Deserialization of a file into an object also known as inflating or 
  unmarshalling.
MARKDOWN """

# MARKDOWN ```

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
with open('c:\\Personal\\tinitiate\\object.pickle', 'wb') as f:
	pickle.dump(Obj1, f)
    
# DeSerialize File to Object
with open('c:\\Personal\\tinitiate\\object.pickle', 'rb') as f:
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
with open('c:\\Personal\\tinitiate\\dict.pickle', 'wb') as f:
	pickle.dump(Dict1, f)

# DeSerialize File to Object
with open('c:\\Personal\\tinitiate\\dict.pickle', 'rb') as f:
	DictFile = pickle.load(f)
    
print(DictFile)

# MARKDOWN ```
