def time_conversion(s):
   
    hour=int(s[0]+s[1])
    if s[9] == "P":
        if hour<12:
            hour+=12
        return(str(hour)+s[2:8])
    elif s[9] == "A":
        if hour == 12:
            hour=00
        return(str(0)+str(hour)+s[2:8])

flag = True
   
def validate(s):
    global flag
    if len(s) == 11:
        if s[10] == 'M' and (s[9] == 'A' or s[9] == 'P'):
            if s[2] == ':' and s[5] == ':' and s[8] == ' ':
                if int(s[0:2]) >=0 and int(s[0:2]) <= 12:
                    if int(s[3:5]) >=0 and int(s[3:5]) < 60:
                        if int(s[6:8]) >= 0 and int(s[6:8]) < 60:
                            return True
    if flag == True:
        flag = False
    else:
        print("Invalid Input. Please enter in correct format!")
    return False
    
if __name__ =="__main__":
    s = ""
    print("Enter the time: (HH:MM:SS PM or HH:MM:SS AM)")
    while not validate(s):
        s = str(input())
    print("Converted Time:", time_conversion(s))
