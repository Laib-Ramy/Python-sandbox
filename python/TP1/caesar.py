
def rotate(c, n):
    if c.isupper():
        return chr((ord(c)-ord('A')+n)%26+ord('A'))
    elif c.islower():
        return chr((ord(c)-ord('a')+n)%26+ord('a'))
    return c

def caesar(plain, n):
    res=""
    for i in plain:
        res+=rotate(i,n)
    return res
def test_caesar():
    if caesar("Hello, world!", 13)=="Uryyb, jbeyq!":
        print("Test of the cipher passed")
    else:
        print("Test of the cipher failed")

test_caesar()

####################### Frequency analysis ###################################

ALPHABET=[chr(x+ord('a')) for x in range(26)]+[chr(x+ord('A')) for x in range(26)]

def freq(s):
    dictio = {letter: 0 for letter in ALPHABET}
    for i in s:
        if i in dictio:
            dictio[i] += 1
    for letter in dictio:
        dictio[letter]= dictio[letter]*100/len("".join(ciphertext.split()))
    return dictio

   

ciphertext="""Te hld l mctrse nzwo olj ty Lactw, lyo esp nwznvd hpcp dectvtyr estceppy.
Htydezy Dxtes, std nsty yfkkwpo tyez std mcplde ty ly pqqzce ez pdnlap esp
gtwp htyo, dwtaapo bftnvwj esczfrs esp rwldd ozzcd zq Gtnezcj Xlydtzyd,
eszfrs yze bftnvwj pyzfrs ez acpgpye l dhtcw zq rcteej ofde qczx pyepctyr
lwzyr htes stx.

Esp slwwhlj dxpwe zq mztwpo nlmmlrp lyo zwo clr xled. Le zyp pyo zq te l
nzwzfcpo azdepc, ezz wlcrp qzc tyozzc otdawlj, slo mppy elnvpo ez esp hlww.
Te opatnepo dtxawj ly pyzcxzfd qlnp, xzcp esly l xpecp htop: esp qlnp zq l
xly zq lmzfe qzcej-qtgp, htes l splgj mwlnv xzfdelnsp lyo cfrrpowj slyodzxp
qplefcpd. Htydezy xlop qzc esp deltcd. Te hld yz fdp ecjtyr esp wtqe. Pgpy
le esp mpde zq etxpd te hld dpwozx hzcvtyr, lyo le acpdpye esp pwpnectn
nfccpye hld nfe zqq ofctyr oljwtrse szfcd. Te hld alce zq esp pnzyzxj octgp
ty acpalcletzy qzc Slep Hppv. Esp qwle hld dpgpy qwtrsed fa, lyo Htydezy,
hsz hld estcej-ytyp lyo slo l glctnzdp fwnpc lmzgp std ctrse lyvwp, hpye
dwzhwj, cpdetyr dpgpclw etxpd zy esp hlj. Zy plns wlyotyr, zaazdtep esp
wtqe-dslqe, esp azdepc htes esp pyzcxzfd qlnp rlkpo qczx esp hlww. Te hld
zyp zq eszdp atnefcpd hstns lcp dz nzyectgpo esle esp pjpd qzwwzh jzf lmzfe
hspy jzf xzgp. MTR MCZESPC TD HLENSTYR JZF, esp nlaetzy mpyples te cly."""

cipherfreq={'a': 19, 'b': 2, 'c': 55, 'd': 58, 'e': 99, 'f': 25, 'g': 12, 
            'h': 26, 'i': 0, 'j': 20, 'k': 3, 'l': 78, 'm': 12, 'n': 29, 
            'o': 35, 'p': 108, 'q': 30, 'r': 23, 's': 56, 't': 65, 'u': 0, 
            'v': 9, 'w': 41, 'x': 20, 'y': 65, 'z': 79, 'A': 0, 'B': 0, 
            'C': 2, 'D': 2, 'E': 4, 'F': 1, 'G': 1, 'H': 5, 'I': 0, 'J': 1, 
            'K': 0, 'L': 3, 'M': 2, 'N': 1, 'O': 0, 'P': 2, 'Q': 0, 'R': 2, 
            'S': 3, 'T': 8, 'U': 0, 'V': 0, 'W': 0, 'X': 1, 'Y': 1, 'Z': 3}

def test_freq():
    if freq(ciphertext)==cipherfreq:
        print("Test of frequency passed")
    else:
        print("Test of frequency failed")

test_freq()

def deceipher(s):
    f = open("big.txt", "r")
    
    return 0

deceipher(ciphertext)