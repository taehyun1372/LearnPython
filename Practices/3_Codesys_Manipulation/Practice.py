import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse("Modbus_Test_Project.xml")
ET.register_namespace('',)
root = tree.getroot()

# Find all Libraries
libraries = root.findall(".//Library")
print("=== Library Original Names ===")
for library in libraries:
    print(library.get("Name"))
    library.attrib["Name"] = "NewName"

# Change the name of Libraries
print("=== Library Editted Names ===")
for library in libraries:
    print(library.get("Name"))

# Add a new element
pous =  root.find(".//pous")
if (pous is not None):
    new_var = ET.SubElement(pous, "variable", {"name": "age"})
    var_type = ET.SubElement(new_var, "type")
    var_type.text = "BOOL"

# Remove an element
# pous =  root.find(".//pous")
# variable = pous.find(".//variable")
# if (variable is not None):
#     pous.remove(variable)

# Save changes
tree.write("Modbus_Test_Project_Edited.xml", encoding="utf-8", xml_declaration=True)

