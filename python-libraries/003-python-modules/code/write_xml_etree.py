import xml.etree.ElementTree as ET

# Generate the XML File
# Create Root Element
root_element = ET.Element("tinitiate")

training_element = ET.SubElement(root_element, "training")

course_element1 = ET.SubElement(training_element, "course")
course_element1.text ='JAVA'
course_element2 = ET.SubElement(training_element, "course")
course_element2.text ='UNIX'

course_element3 = ET.SubElement(training_element, "course")
course_element3.text ='PERL'
course_element4 = ET.SubElement(training_element, "course")
course_element4.text ='PYTHON'

code_element1 = ET.SubElement(root_element, "code")
code_element1.set("id",str(1))
code_element1.text ='Python XML Parsing'

code_element2 = ET.SubElement(root_element, "code")
code_element2.set("id",str(2))
code_element2.text ='Python File writing'


# create a new XML file with the results
mydata = ET.tostring(root_element, encoding='unicode')
print(mydata)

# Write the Generated XML to file
myfile = open("E:\\python-master\\media\\test-data-OUT.xml", "w")
myfile.write(mydata)