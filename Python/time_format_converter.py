def time_conversion(s):

    hour=int(s[0]+s[1])
    if s[8] == "P":
        if hour<12:
            hour+=12
        return(str(hour)+s[2:8])
    elif s[8] == "A":
        if hour == 12:
            hour=00
        return(str(0)+str(hour)+s[2:8])

if __name__ =="__main__":
    print("Enter the time: (HH:MM:SSPM or HH:MM:SSAM") #Here the last two characters of the string denotes AM or PM"
    s = input()
    result = time_conversion(s)
