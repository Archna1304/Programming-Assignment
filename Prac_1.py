print("Archana Vyas 20CE157")
def frequency():
    
    s1="aabbccd"
    s2={}
    for i in s1:
        if i not in s2:
            s2[i.lower()]=1
        else:
            s2[i.lower()] =s2[i.lower()]+1 
    print(s2)
frequency()
