def numberOfBits(n):

    count = 0 
    while(n):
        count = count + 1
        n>>= 1
    
    return count

number =  int(input("Enter your number= "))
print("total bits  =  ",numberOfBits(number))