#the code bellow gives you your ip address lets you see your subnet if youknow your subnetmask and gives you your location and many move information about it
#or if you choose to submit an ip of your choice give you its binary writing and subnet if you give the subnet mask 




import json
import re
import requests

#fonction get location
def get_location(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()
        location_data = json.loads(response.text)
        return location_data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during request: {str(e)}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {str(e)}")
        return None
#fonction de verification de la validité sur masque d esous reseau
def est_subnetmask(subnet):
    subnetmask_regex= r'^(?:\b(128|192|224|240|248|252|254|255|0)\b\.){3}\b(128|192|224|240|248|252|254|255|0)\b$'

    if re.match(subnetmask_regex, subnet):
        return True
    else:
        return False
#verification de la validité de l'ipv4
def est_ipv4(adresse):
    regex_ipv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    resultat = re.match(regex_ipv4, adresse)
    if resultat:
        return True
    else:
        return False
#fonction de convertion de d'une ip en binaire
def convertion_binaire(adresse_ip,x=0):
    parties = adresse_ip.split('.')
    parties_binaires = []
    
    for partie in parties:
        partie_binaire = bin(int(partie))[2:].zfill(8)
        parties_binaires.append(partie_binaire)
    
    adresse_binaire = '.'.join(parties_binaires)
    adresse_binaire_calcul=''.join(parties_binaires)
    if (x==1):
        return adresse_binaire_calcul
    
    else:
        return adresse_binaire
#fonction de calcul du sous reseau
def subnet(host,sub):
    host=convertion_binaire(host,1)
    sub=convertion_binaire(sub,1)
    subnet=int(host,2) & int(sub,2)
    subnet=bin(subnet)[2:].zfill(32)
    subnet=str(subnet)
    y = 0
    for i in range(len(sub)):
        if sub[i] != "1" :
            break
        else :
            y += 1
    subnetip=[]
    for i in range(0,32,8):
        subnetip.append(str(int(subnet[i:i+8],2)))
    subnet='.'.join(subnetip)
    return subnet+"/"+str(y)
#fonction de recuperation de l'ip public de l'utilisateur
def get_external_ip():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    ip_address = data['ip']
    return ip_address
#programme principale
def main():
    validip=False
    validsubmask=False
    for i in range(30):
                print("- ",end=' ')
    print("")
    ans=str(input("use your IP ?                    |  Y/N   "))
    for i in range(30):
        print("- ",end=" ")
    print("")
    if ans.upper()== "N":
        #input
        while not validip :
            ip= (input("give me an ip or use default     | default=192.168.1.100  my input= ") or "192.168.1.100")
            for i in range(30):
                print("- ",end=" ")
            print("")
            validip=est_ipv4(ip)
            if not validip:
                print("                     !>IP non valide recommencer<!  ")
                for i in range(30):
                    print("- ",end=" ")
                print("")
        print("                            !>IP valide<!")
        for i in range(30):
            print("- ",end=" ")
        print("")
    else:
        ip=get_external_ip()
        print("your IP ADDRESS is               | ",ip)
        for i in range(30):
            print("- ", end=" ")
        print("")
    while not validsubmask :
        subnetmask=(input("give subnet or use default       | default=255.255.255.0  my input= ") or "255.255.255.0")
        for i in range(30):
            print("- ",end=' ')
        print("")
        validsubmask=est_subnetmask(subnetmask)
        if not validsubmask:
            print("           !>masque de sous reseau non valide recommencer<!  ")
            for i in range(30):
                print("- ",end=' ')
            print("")
    print("                  !>masque de sous reseau valide<!")
    for i in range(30):
        print("- ",end=" ")
    print("")
    #affichage des resultats
    print("l'ip en binaire                  | ",convertion_binaire(ip))
    for i in range(30):
        print("- ",end=" ")
    print("")
    print("le masque sous reseau en binaire | ",convertion_binaire(subnetmask))
    for i in range(30):
        print("- ",end=" ")
    print("")
    sous_reseau=subnet(ip,subnetmask)
    print("le sous reseau est               | ", sous_reseau)
    for i in range(30):
        print("- ",end=" ")
    print("")
    z=sous_reseau.split("/")[1]
    z=int(z)
    print("le nombre d'hote                 | ",2**(32-z)-2)
    for i in range(30):
        print("- ",end=" ")
    print("")

    location = get_location(ip)
    if (location is not None):
        if "bogon" not in location:
            print("Informations de localisation de  | ",ip)
            for i in range(30):
                print("- ",end=" ")
            print("")
            print("Pays                             | ", location['country'])
            for i in range(30):
                print("- ",end=" ")
            print("")
            print("Ville                            | ", location['city'])
            for i in range(30):
                print("- ",end=" ")
            print("")
            print("Région                           | ", location['region'])
            for i in range(30):
                print("- ",end=" ")
            print("")
            print("Code postal                      | ", location['postal'])
            for i in range(30):
                print("- ",end=" ")
            print("")
            print("Coordonnées                      | ", location['loc'])
            for i in range(30):
                print("- ",end=" ")
            print("")
        elif location is None:
            print("                 !>erreur localisation introuvable<!")
            for i in range(30):
                print("- ",end=" ")
            print("")
        elif location['bogon']==True:
            print("                   !>erreur adresse IP réservées<!")
            for i in range(30):
                print("- ",end=" ")
            print("")
    elif location is None:
        print("                 !>erreur localisation introuvable<!")
        for i in range(30):
            print("- ",end=" ")
        print("")
    elif location['bogon']==True:
        print("                   !>erreur adresse IP réservées<!")
        for i in range(30):
            print("- ",end=" ")
        print("")
main() 
"""
#bonus convertion d'une ip en hexadecimal
def convertion_hexadecimal(adresse_ip):
    parties = adresse_ip.split('.')
    parties_hexa = []
    
    for partie in parties:
        partie_hexa = hex(int(partie))[2:].zfill(2)
        parties_hexa.append(partie_hexa)
    
    adresse_hexa = '.'.join(parties_hexa)
    return adresse_hexa
print("l'ip en hexadecimal              | ",convertion_hexadecimal(ip))
for i in range(30):
   print("- ",end=" ")
print("")
"""
