import xml.etree.ElementTree as ET

def strip_namespaces(elem):
    """Recursively remove all namespaces from XML element tags."""
    for el in elem.iter():
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
        # Also strip attribute namespaces if needed
        el.attrib = {k.split('}', 1)[-1] if '}' in k else k: v for k, v in el.attrib.items()}

tree = ET.parse("Modbus_Test_Project2.xml")
root = tree.getroot()
strip_namespaces(root)
tree.write("Modbus_Test_Project_Test5.xml", encoding="utf-8", xml_declaration=True)

