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

if __name__ =="__main__":
    print("Enter the time: (HH:MM:SS PM or HH:MM:SS AM)") #Here the last two characters of the string denotes AM or PM"
    s = input()
    print("Converted Time: ", time_conversion(s))
