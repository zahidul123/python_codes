varRange=int(input("Enter the range of number: "))
varCountnumber=int(input("Counting number In Decimal point :"))
if varRange is 1 and varCountnumber is 1:
    print("number of palindrome is 1")
if varRange is 2 and varCountnumber is 1:
    print("number of palindrome is 2")
if varRange and varCountnumber >= 2:
    if varRange >= varCountnumber:
        if varCountnumber%2 is 0 :
            print("number of palindrome is ",varRange**(varCountnumber/2) )
        else:
            print("number of palindrome is ", varRange**(int(varCountnumber/2)+1))
    elif varCountnumber>varRange:
        if varCountnumber%2 is 0 :
            print("number of palindrome is ",varCountnumber )
        else:
            print("number of palindrome is ", varCountnumber+1)