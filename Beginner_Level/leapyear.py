year = int(input("Please Enter the Year: "))
 
if (( year%4 == 0 ) and ( year%100 != 0)):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
