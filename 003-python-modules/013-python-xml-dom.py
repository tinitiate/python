#========================================================================================
# TOPIC: PYTHON - XML DOM Programming
#========================================================================================
# NOTES: * PYTHON provides mechanisms to parse and examin XML files
#        * This program demonstrated DOM parsing of the test XML, in PYTHON
#        * The Document Object Model (DOM), its very useful to randomly 
#          access elements of an XML.
#        * this program uses xml dom minidom
#        * First operation is to parse the XML document
#        * Each XML is made up of elements, its values (Optional) and attributes  
#          (optional) .The trick is to get the An XML ELEMENT using getElementsByTagName,
#          with in that extract the element value and attribute as needed
#        
#========================================================================================
#
# FILE-NAME       : 033_python_xml_dom.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   text.xml (This is included in the comments in the program
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2014
#
# DESC            : PYTHON XML Programming
#
#========================================================================================

###########
# text.xml
###########
# Save the following in c:\tinitiate\text.xml file
# -- test.xml START --
#<tinitiate>
#    <training>
#        <course>JAVA</course>
#        <course>UNIX</course>
#        <course>PERL</course>
#        <course>PYTHON</course>
#    </training>
#    <code id="1"> Python XML Parsing </code>
#    <code id="2"> Python File writing </code>
#</tinitiate>
# -- test.xml END --

# IMPORT the XML.DOM minidom module
from xml.dom import minidom


# Create a DOM object by reading the XML
xmldoc = minidom.parse('c:\\tinitiate\\test.xml')


# Extract the TINITIATE element and its children from the xmldoc
tinitiate_elements = xmldoc.getElementsByTagName("tinitiate")


# Since we know the tinitiate element has children we use the loop
for tinitiate_element in tinitiate_elements:
    # For every tinitiate element, extract the next clind node, i.e, training
    training_elements = tinitiate_element.getElementsByTagName("training")


    # Get Values of the training_elements list
    for training_element in training_elements:
        # For every course element, extract the next clind node, i.e, COURSE
        course_elements = training_element.getElementsByTagName("course")


        # Get Values of the course_elements list
        for course_element in course_elements:
            # For every course element, print the nodeValue,
            # NOTE: There is only ONE child Node at the lowest level so use index ZERO
            print(course_element.childNodes[0].nodeValue)


    # READING Attributes, in CODE element which is at the same level
    # as the training_element
    code_elements = xmldoc.getElementsByTagName("code")

    print("Total Count of 'CODE' elements in XML: ",len(code_elements))

    # Loop through the code_elements list
    for code_element in code_elements:

        # print the attributes of every code_element
        print(code_element.attributes["id"].value)
        # print the NodeValue of every code_element
        print(code_element.childNodes[0].nodeValue)


#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: PYTHON - XML parsing python DOM SAX parsing tutorial
#
#========================================================================================
