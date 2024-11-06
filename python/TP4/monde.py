import xml.etree.ElementTree as ET

class Monde:
    def __init__(self):
        self.tree=ET.parse('mondial-3.0.xml')
        self.root=self.tree.getroot()
        
    def regime(self, country):
            c=self.tree.find(f'country[@name="{country}"]')
            if c :
                return c.get('government')
            raise ValueError(f"Le pays '{country}' est introuvable dans la base de données.")
        
    

