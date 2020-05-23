 for i in range(1,101):
	if i%7==0: #7 de bei shu 
		continue
	elif i%10==7: # ge wei  shi 7
		continue
	elif i//10 == 7:  # shi wei shi 7
		continue
	else:
		print(i)

