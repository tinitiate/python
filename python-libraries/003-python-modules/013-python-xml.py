""" MARKDOWN
---
Title: Python XML
Tags: Python XML, SAX, DOM, Read XML, Write to XML
Author: Venkata Bhattaram /  www.github.com/tinitiate
ContentName: python-xml
---
MARKDOWN """

""" MARKDOWN
# Python XML Module
* Here we demonstrate the following
  * Read from an XML file using DOM
  * Read from an XML file using SAX
  * Write to XML

## Python Read XML using Mini DOM
* Here we demonstrate XML DOM parsing using the `minidom` module.
* The Document Object Model (DOM), its very useful to randomly 
  access elements of an XML.
* First operation is to parse the XML document
* Each XML is made up of elements, its values (Optional) and attributes  
  (optional) .The trick is to get the An XML ELEMENT using getElementsByTagName,
  with in that extract the element value and attribute as needed
* Below is the XML, that will be used in the demo.
* Save the file as `test-data.xml` in `c:/tinitiate` folder
MARKDOWN """
# MARKDOWN```xml
# <tinitiate>
#     <training>
#         <course>JAVA</course>
#         <course>UNIX</course>
#         <course>PERL</course>
#         <course>PYTHON</course>
#     </training>
#     <code id="1"> Python XML Parsing </code>
#     <code id="2"> Python File writing </code>
# </tinitiate>
# MARKDOWN```

# MARKDOWN```python
from xml.dom import minidom

# Create a DOM object by reading the XML
# xmldoc = minidom.parse('C:/tinitiate/test-data.xml')
xmldoc = minidom.parse('C:/tinitiate/test-data.xml')

# Print the document node and name of the first child tag
print (xmldoc.nodeName)
print (xmldoc.firstChild.tagName)

################################################################################
# Extract Tag and its elements By Tag Name
################################################################################
# Extract the TINITIATE element and its children from the xmldoc
tinitiate_elements = xmldoc.getElementsByTagName("tinitiate")


################################################################################
# Loop through a Tag Element and read underlying Elements / Attributes
################################################################################
# Since we know the tinitiate element has children we use the loop
for tinitiate_element in tinitiate_elements:

    # For every tinitiate element, extract the next clind node, i.e, training
    training_elements = tinitiate_element.getElementsByTagName("training")


    # Get Values of the training_elements list
    ##########################################
    for training_element in training_elements:

        # For every course element, extract the next clind node, i.e, COURSE
        course_elements = training_element.getElementsByTagName("course")

        # Get Values of the course_elements list
        for course_element in course_elements:
            # For every course element, print the nodeValue,
            # NOTE: There is only ONE child Node at the lowest
            #       level so use index ZERO
            print(course_element.childNodes[0].nodeValue)


    # READING Attributes, in CODE element which is at 
    # the same level as the training_element
    ###################################################
    code_elements = xmldoc.getElementsByTagName("code")

    # Print the number of elements with in a Tg    
    print("Total Count of 'CODE' elements in XML: ",len(code_elements))


    # Loop through the code_elements list
    #####################################
    for code_element in code_elements:

        # print the attributes of every code_element
        print(code_element.attributes["id"].value)
        # print the NodeValue of every code_element
        print(code_element.childNodes[0].nodeValue)

# MARKDOWN```


""" MARKDOWN
## Python Read XML using SAX
* This program demonstrated SAX parsing of the test XML, in PYTHON
* The Simple API for XML (SAX), its very useful to parse large XMl documents 
  access elements of an XML. The entire document is NEVER loaded into memory,
  only the portions based on an element name are loaded, 
* this program uses python xml.SAX module
* Using SAX requires the developer to write Contenthandler by creating a 
  subclass of xml.sax.ContentHandler
* startDocument and endDocument
* characters() method is invoked whenever character data is found.
* First operation is to parse the XML document
* Each XML is made up of elements, its values (Optional) and attributes 
  (optional) The trick is to get the An XML ELEMENT using getElementsByTagName,
  with in that extract the element value and attribute as needed.
* Below is the XML, that will be used in the demo.
* Save the file as `test-data.xml` in `c:/tinitiate` folder
MARKDOWN """
# MARKDOWN```xml
# <tinitiate>
#     <training>
#         <course>JAVA</course>
#         <course>UNIX</course>
#         <course>PERL</course>
#         <course>PYTHON</course>
#     </training>
#     <code id="1"> Python XML Parsing </code>
#     <code id="2"> Python File writing </code>
# </tinitiate>

# MARKDOWN```python
import xml.sax

# Create Class With the Constructor / StartElement / EndElement methods
class TIContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.CurrentData = ""
        
    def startElement(self, name, attrs):
        print("startElement :" + name)
        self.CurrentData = name
        if name == "code":
            print("\tattribute id=" + attrs.getValue("id"))
    
    def characters(self, content):
        if self.CurrentData == "course":
            print(content)

        if self.CurrentData == "code":
            print(content)

    def endElement(self, name):
        print("endElement:"  + name)


def SAXprocessXML(sourceFileName):
  source = open(sourceFileName)
  xml.sax.parse(source, TIContentHandler())

# SAXprocessXML('c:\\tinitiate\\test.xml')
SAXprocessXML('C:/tinitiate/test-data.xml')

# MARKDOWN```


""" MARKDOWN
## Python Create and Write to XML using ElementTree
* The ElementTree module, provides the following
  * ElementTree.Element : Creates the Root Element
  * ElementTree.SubElement : Creates the Sub Element
  * ElementTree.SubElement.text : Sets the Element Value
  * ElementTree.SubElement.set("id","Value") : Set the Attribute Name and Value
MARKDOWN """
# MARKDOWN```
import xml.etree.ElementTree as ET

# Generate the XML File
# Create Root Element
root_element = ET.Element("tinitiate")

# Create Sub Element
training_element = ET.SubElement(root_element, "training")
course_element1 = ET.SubElement(training_element, "course")

# Set Sub Element Value
course_element1.text = "JAVA"
course_element2 = ET.SubElement(training_element, "course")
course_element2.text = "UNIX"
course_element3 = ET.SubElement(training_element, "course")
course_element3.text = "PERL"
course_element4 = ET.SubElement(training_element, "course")
course_element4.text = "PYTHON"
code_element1 = ET.SubElement(root_element, "code")

# Set Attribute
code_element1.set("id",str(1))
code_element1.text = "Python File Reading"
code_element2 = ET.SubElement(root_element, "code")
code_element2.set("id",str(2))
code_element2.text = "Python File Writing"

# create a new XML file with the results
mydata = ET.tostring(root_element, encoding='unicode')
print(mydata)

# Write the Generated XML to file
myfile = open("C:/tinitiate/test-data-OUT.xml", "w")
myfile.write(mydata)
# MARKDOWN```
