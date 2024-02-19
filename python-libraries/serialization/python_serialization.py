# Python Pickle Serialization and De-Serialization
# #################################################################
#* Serialization is the process of converting an object state into a 
#  binary file, this file can be stored on filesystem or transmitted across
#  network. or it can be persisted(stored) and later use. 
#* Serialization of an object is also known as deflating or marshalling.
#* In Python we use the **PICKLE** module to Serialize an Object.
#* In order to resurrect an Object from a Pickle file it needs to be deserialized
#* Deserialization of a file into an object also known as inflating or 
#  unmarshalling.
import pickle

#############################
# Serialization of an Object
#############################

# Create a Class
class PickleTest():
    # Class Variables
    a=0
    b=0
    # Constructor
    def __init__(self,i_a,i_b):
        self.a=i_a
        self.b=i_b


# Create an Object
Obj1 = PickleTest(1,2)

l_serialization_loc = "D:\\training\\PythonFeb2024\\code\\python-libraries\\serialization/object.pickle"

# Serialize an Object
with open(l_serialization_loc, 'wb') as f:
	pickle.dump(Obj1, f)

# With is same as below
# ####################################
# f = open(l_serialization_loc, 'wb')
# pickle.dump(Obj1, f)
# f.close()


# DeSerialize File to Object
# #############################
l_serialization_loc = "D:\\training\\PythonFeb2024\\code\\python-libraries\\serialization/object.pickle"
with open(l_serialization_loc, 'rb') as f:
	ObjFile = pickle.load(f)

print(ObjFile)
print(ObjFile.a)
print(ObjFile.b)
