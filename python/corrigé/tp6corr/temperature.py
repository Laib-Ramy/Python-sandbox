from urllib import request
import xml.etree.ElementTree as et

def temperature(ville):
    url=f'https://api.openweathermap.org/data/2.5/weather?q={ville}&appid=29f14a7a8876ecb1219ecccd26ce4c1e&mode=xml'
    response = request.urlopen(url).read()
    tree = et.fromstring(response)
    t=tree.find("./temperature").attrib['value']
    return float(t)-273.16

