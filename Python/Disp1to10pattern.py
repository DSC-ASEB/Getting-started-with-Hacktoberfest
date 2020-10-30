currentNumber = 1
rows = 4  # Rows you want in your pattern
stop = 2
for i in range(rows):
    for column in range(1, stop):
        print(currentNumber, end=' ')
        currentNumber += 1
    print("")
    stop += 1
