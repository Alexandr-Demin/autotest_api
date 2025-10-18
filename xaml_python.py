import xml.etree.ElementTree as ET


xaml_data = """
<user>
    <id>1</id>
    <ferst_name>Jon</ferst_name>
    <Last_name>Dor</Last_name>
    <email>jon@email.com</email>
</user>
""" 
root = ET.fromstring(xaml_data)

print("User ID:", root.find('id').text)



