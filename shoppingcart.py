import random
a=input("Enter your name:")
price=0
cart=[]
captcha=["aiWqrcf","ffvrE","erGHi5","effDGD","rgthFGH"]
i=0
while i==0:
	print("sports,sanitary,stationery,bags")
	b=input("select any of these above categories or if you want to checkout press checkout:")
	if(b=="sports"):
		print("select any of cricket bat,badminton racket,football,shuttle cocks,balls")
		c=input("select any of the above:")
		if(c=="bat" or c=="cricket bat"):
			print("adidas-1500")
			print("nike-1200")
			print("rebook-1350")
			d=input("any of the above companies:")	
			if(d=="adidas"):
				cart.append(d)
				price=price+1500
			elif(d=="nike"):
				cart.append(d)
				price=price+1200
			elif(d=="rebook"):
				cart.append(d)
				price=price+1350	
		elif(c=="racket" or "badminton racket"):
			print("yonex-1700")
			print("lining-1560")
			print("head-2400")
			d=input("any of the above companies:")	
			if(d=="yonex"):
				cart.append(d)
				price=price+1700
			elif(d=="lining"):
				cart.append(d)
				price=price+1560
			elif(d=="head"):
				cart.append(d)
				price=price+2400	
		elif(c=="football"):								
			print("adidas-1500")
			print("nike-1200")
			print("rebook-1350")
			d=input("any of the above companies:")
			if(d=="adidas"):
				cart.append(d)
				price=price+1500
			elif(d=="nike"):
				cart.append(d)
				price=price+1200
			elif(d=="rebook"):
				cart.append(d)
				price=price+1350
		elif(c=="cocks" or "shuttle cocks"):
			print("yonex-170")
			print("lining-156")
			print("head-240")
			d=input("any of the above companies:")
			if(d=="yonex"):
				cart.append(d)
				price=price+170
			elif(d=="lining"):
				cart.append(d)
				price=price+156
			elif(d=="head"):
				cart.append(d)
				price=price+240
		elif(c=="balls"):
			print("cork ball-200")
			print("tennis ball-55")
			print("stumper ball-40")
			d=input("any of the balls:")
			if(d=="cork balls"):
				cart.append(d)
				price=price+200
			elif(d=="tennis ball"):
				cart.append(d)
				price=price+55
			elif(d=="stumper ball"):
				cart.append(d)
				price=price+40
	if(b=="sanitary"):
		print("select any of soaps,shampoos,facewash")
		c=input("select any of the above:")
		if(c=="soaps"):
			print("dettol-20")
			print("cintol-25")
			print("santoor-30")
			d=input("any of the above companies:")	
			if(d=="dettol"):
				cart.append(d)
				price=price+20
			elif(d=="cintol"):
				cart.append(d)
				price=price+25
			elif(d=="santoor"):
				cart.append(d)
				price=price+30
		elif(c=="shampoos"):
			print("clinic plus-50")
			print("pantene-65")
			print("meera-60")
			d=input("any of the above companies:")	
			if(d=="clinic plus"):
				cart.append(d)
				price=price+50
			elif(d=="pantene"):
				cart.append(d)
				price=price+65
			elif(d=="meera"):
				cart.append(d)
				price=price+60
		elif(c=="facewash"):								
			print("patangali-145")
			print("nivea-155")
			print("garnier-150")
			d=input("any of the above companies:")
			if(d=="patanjali"):
				cart.append(d)
				price=price+145
			elif(d=="nivea"):
				cart.append(d)
				price=price+155
			elif(d=="garnier"):
				cart.append(d)
				price=price+150
	if(b=="stationery"):
		print("select any of pens,pencils,erasers")
		c=input("select any of the above:")
		if(c=="pens" or c=="pen"):
			print("renolds-10")
			print("parker-250")
			print("cello-15")
			d=input("any of the above companies:")	
			if(d=="renolds"):
				cart.append(d)
				price=price+10
			elif(d=="parker"):
				cart.append(d)
				price=price+250
			elif(d=="cello"):
				cart.append(d)
				price=price+15
			
		elif(c=="pencils" or c=="pencil"):
			print("doms-5")
			print("apasara-6")
			print("natraj-4")
			d=input("any of the above companies:")	
			if(d=="doms"):
				cart.append(d)
				price=price+5
			elif(d=="apasara"):
				cart.append(d)
				price=price+6
			elif(d=="natraj"):
				cart.append(d)
				price=price+4
			
		elif(c=="erasers" or c=="eraser"):								
			print("apasara-5")
			print("doms-15")
			print("natraj-10")
			d=input("any of the above companies:")
			if(d=="apasara"):
				cart.append(d)
				price=price+5
			elif(d=="doms"):
				cart.append(d)
				price=price+15
			elif(d=="natraj"):
				cart.append(d)
				price=price+10
			
						
	if(b=="bags"):
		print("select any of college bags,tourist bags")
		c=input("select any of the above:")
		if(c=="college bags" or "college"):
			print("skybags-1560")
			print("wildcraft-1400")
			print("american tourister-1655")
			d=input("any of the above companies:")	
			if(d=="skybags"):
				cart.append(d)
				price=price+1560
			elif(d=="wildcraft"):
				cart.append(d)
				price=price+1400
			elif(d=="american tourister"):
				cart.append(d)
				price=price+1655	
		elif(c=="tourist bags" or "tourist"):
			print("vip-1450")
			print("american tourister-1300")
			d=input("any of the above companies:")	
			if(d=="vip"):
				cart.append(d)
				price=price+1450
			elif(d=="american tourister"):
				cart.append(d)
				price=price+1300
	
		
	if(b=="checkout"):
		i+=1
	
if(i==1):
	print(" items in our cart:",cart)
	print("do you have any coupons:")
	coup=input("yes or no:")
	if(coup=="yes"):
		price=price-price*4/100
		print("price of items in cart:",price)
	else:
		print("price of items in cart:",price)		
	if(price>0):
		print("to proceed through payment please enter the captcha")
		read=random.choice(captcha)
		print(read)
		pay=input()
		if(pay==read):
			amt=int(input("enter the amount you have to pay:"))
			if(amt==price):
				card=int(input("enter your card number:"))
				print("Your payement is sucessuful")
				print("Thanks for shopping with us")
			else:
				print("please check the amount you have to pay") 
		else:
			print("error please try the captcha again")
			read=random.choice(captcha)
			print(read)
			pay=input()
			if(pay==read):
				amt=int(input("enter the amount you have to pay:"))
				if(amt==price):
					card=int(input("enter your card number:"))
					print("Your payement is sucessuful")
					print("Thanks for shopping with us")
