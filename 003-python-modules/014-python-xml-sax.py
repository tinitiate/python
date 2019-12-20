#========================================================================================
# TOPIC: PYTHON - SAX XML Parsing
#========================================================================================
# NOTES: * PYTHON provides mechanisms to parse and examine XML files
#        * This program demonstrated SAX parsing of the test XML, in PYTHON
#        * The Simple API for XML (SAX) , its very useful to parse large XMl documents 
#          access elements of an XML. The entire document is NEVER loaded into memory,
#          only the portions based on an element name are loaded, 
#        * this program uses python xml.SAX module
#        * Using SAX requires the developer to write Contenthandler by creating a 
#          subclass of xml.sax.ContentHandler
#        * startDocument and endDocument
#        * characters() method is invoked whenever character data is found.
#        * First operation is to parse the XML document
#        * Each XML is made up of elements, its values (Optional) and  
#          attributes (optional) The trick is to get the An XML ELEMENT using 
#          getElementsByTagName, with in that extract the element value and attribute 
#		   as needed
#        
#========================================================================================
#
# FILE-NAME       : 034_python_xml_sax_parsing.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   text.xml (This is included in the comments in the program
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2014
#
# DESC            : PYTHON Database programming
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

# IMPORT the XML.sax module
import xml.sax

class TIContentHandler(xml.sax.ContentHandler):
  def __init__(self):
    xml.sax.ContentHandler.__init__(self)

  def startElement(self, name, attrs):
    print("startElement :" + name)
    if name == "code":
      print("\tattribute id=" + attrs.getValue("id"))

  def endElement(self, name):
    print("endElement:"  + name)

def SAXprocessXML(sourceFileName):
  source = open(sourceFileName)
  xml.sax.parse(source, TIContentHandler())

SAXprocessXML('c:\\tinitiate\\test.xml')


#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: PYTHON - XML parsing python DOM SAX parsing tutorial
#
#========================================================================================
