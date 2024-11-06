import xml.etree.ElementTree as ET

class Monde:
    def __init__(self):
        self.tree = ET.parse('mondial-3.0.xml')

    def regime(self, country):
        root=self.tree.getroot()
        path=f"./country[@name='{country}']"
        c=root.find(path)
        if c is None:
            raise ValueError("No such country")
        return c.attrib['government']
        


