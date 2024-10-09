import re
t=r'01-69-15-69-39'
def internationalize(tel):
    pattern=r"^((0)[1-9])((-)\d{2}){4}$"
    pattern2=r"^(0)"
    pat3="+33-"
    if re.fullmatch(pattern,tel):
        res=re.sub(pattern2,pat3,tel)
        return res
    else:
        raise ValueError
    
print(internationalize(t))
    