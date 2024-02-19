from xml.dom import minidom

# Create a DOM object by reading the XML
# xmldoc = minidom.parse('C:/tinitiate/test-data.xml')
# Note: Change the folder to where the file is located
xmldoc = minidom.parse('E:/python-master/media/003-python-modules/test-data.xml')

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
