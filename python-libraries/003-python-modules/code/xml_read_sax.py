import xml.sax

# Define a class that inherits from xml.sax.ContentHandler
class TIContentHandler(xml.sax.ContentHandler):
    # Constructor method
    def __init__(self):
        # Call the constructor of the base class
        xml.sax.ContentHandler.__init__(self)
        # Initialize a variable to keep track of the current element being parsed
        self.CurrentData = ""
        
    # This method is called every time a new element is encountered in the XML file
    def startElement(self, name, attrs):
        # Print the name of the element
        print("startElement :" + name)
        # Update the value of the current data variable
        self.CurrentData = name
        # If the current element is "code", print its "id" attribute value
        if name == "code":
            print("\tattribute id=" + attrs.getValue("id"))
    
    # This method is called every time character data is encountered inside an element
    def characters(self, content):
        # If the current element is "course", print its value
        if self.CurrentData == "course":
            print(content)
        # If the current element is "code", print its value
        if self.CurrentData == "code":
            print(content)

    # This method is called every time the end of an element is encountered
    def endElement(self, name):
        # Print the name of the element
        print("endElement:"  + name)


# This function processes an XML file using the SAX parser and the TIContentHandler class
def SAXprocessXML(sourceFileName):
  # Open the XML file for reading
  source = open(sourceFileName)
  # Parse the XML file using the SAX parser and the TIContentHandler class
  xml.sax.parse(source, TIContentHandler())

# Call the SAXprocessXML function with the path to the XML file as an argument
# Note: Change the folder to where the file is located
SAXprocessXML('E:/python-master/media/003-python-modules/test-data.xml')
