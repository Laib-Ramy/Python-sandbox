def pgcd(a,b):
    a1=max(a,b)
    b2=min(a,b)
    if b2 == 0:
        return a1
    else :
        return pgcd (b2 , a1 % b2 )

def phi(n):
    cpt=0
    for i in range(n):
        if (pgcd(n,i)==1):
            cpt+=1
    return cpt
            

##########################################################################
############### Do not modify the file below this line ###################


pgcdval=[(42, 15, 3), (52, 37, 1), (97, 57, 1), (62, 87, 1), (64, 91, 1), 
         (41, 91, 1), (24, 14, 2), (22, 90, 2), (69, 22, 1), (87, 14, 1), 
         (46, 76, 2), (45, 20, 5), (50, 14, 2), (82, 13, 1), (61, 81, 1), 
         (55, 34, 1), (79, 95, 1), (44, 58, 2), (37, 37, 37), (48, 40, 8)]

def test_pgcd():
    passed=True
    for a,b,c in pgcdval:
        if c!= pgcd(a,b):
            passed=False
            print(f"Test pgcd failed: pgcd({a}, {b}) = {c} != {pgcd(a,b)}")
            break
    if passed:
        print("Test pgcd passed")

test_pgcd()

phival=[(1, 1), (2, 1), (3, 2), (4, 2), (5, 4), (6, 2), (7, 6), (8, 4), 
        (9, 6), (10, 4), (11, 10), (12, 4), (13, 12), (14, 6), (15, 8), 
        (16, 8), (17, 16), (18, 6), (19, 18), (20, 8), (21, 12), (22, 10), 
        (23, 22), (24, 8)]

def test_phi():
    passed=True
    for a,b in phival:
        if(b!=phi(a)):
            passed=False
            print(f"Test phi failed: phi({a}) = {b} != {phi(a)}")
            break
    if passed:
        print("Test phi passed")

test_phi()
