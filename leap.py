year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")


#  =======================================

###it my second logic to solve leap year###
user=int(input('Enter the year >'))
if user%4==0:
    if user%100==0:
        if user%400==0:
		    print( "it's leap year")
        else:
            print("it's not a leap")
    else:
        print("It's leap year")
else:
	print ("it's not leap year")
