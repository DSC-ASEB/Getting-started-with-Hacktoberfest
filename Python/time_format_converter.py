def time_conversion(s):
    assert s[10] == 'M' and (s[9] == 'A' or s[9] == 'P') , "Please enter in the valid format!"
    assert s[2] == ':' and s[5] == ':' and s[8] == ' ', "Please enter in the valid format!"
    hour=int(s[0]+s[1])
    if s[9] == "P":
        if hour<12:
            hour+=12
        return(str(hour)+s[2:8])
    elif s[9] == "A":
        if hour == 12:
            hour=00
        return(str(0)+str(hour)+s[2:8])
    
    
if __name__ =="__main__":
    s = ""
    print("Enter the time: (HH:MM:SS PM or HH:MM:SS AM)")
    while len(s) < 11:
        s = input()
        if len(s) < 11:
            print("Invalid Input.Enter the value again!")
    print("Converted Time: ", time_conversion(s))
