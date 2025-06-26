import xml.etree.ElementTree as ET

# Load the XML file

tree = ET.parse("sample.xml")
root = tree.getroot()

# Find all POUs
pous = root.findall(".//pou")
print("=== POU Names ===")
for pou in pous:
    print(pou.attrib["name"])

# Modify body of MAIN program
for pou in pous:
    if pou.attrib.get("name") == "MAIN":
        st_node = pou.find(".//ST")
        if st_node is not None:
            st_node.text = "start := NOT start;"  # Replace existing code
            print("\nModified MAIN POU body.")
        break

# Add a new input variable
for pou in pous:
    if pou.attrib.get("name") == "MAIN":
        input_vars = pou.find(".//inputVars")
        if input_vars is not None:
            new_var = ET.Element("variable", {"name": "stop"})
            var_type = ET.SubElement(new_var, "type")
            ET.SubElement(var_type, "BOOL")  # <type><BOOL/></type>
            input_vars.append(new_var)
            print("Added new variable: stop")
        break

# Save the modified XML
tree.write("sample_edited.xml", encoding="utf-8", xml_declaration=True)
