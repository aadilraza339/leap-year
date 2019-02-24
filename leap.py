user=int(raw_input('Enter the year >'))
if user%4==0:
	if user%400==0 and user%100==0:
		print 'leap hai'
else:
	print 'leap year nahi hai'