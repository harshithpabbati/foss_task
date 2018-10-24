import random
c=int(input("how many attempts???"))
list=["stone","paper","scissors"]
cpu=0
yourscore=0
for i in range(c):
	a=random.choice(list)
	b=input("any of stone,paper,scissors:")
	if(a=="stone" and b=="paper"):
		yourscore+=1
		print("cpu's choice",a)
		print("yourscore:",yourscore)
		print("cpu:",cpu)
	elif(a=="stone" and b=="scissors"):
		cpu+=1
		print("cpu's choice",a)
		print("yourscore:",yourscore)
		print("cpu:",cpu)
	elif(a=="paper" and b=="stone"):
		cpu+=1
		print("cpu's choice",a)
		print("yourscore:",yourscore)
		print("cpu:",cpu)
	elif(a=="paper" and b=="scissors"):
		yourscore+=1
		print("cpu's choice",a)
		print("yourscore:",yourscore)
		print("cpu:",cpu)
	elif(a=="scissors" and b=="paper"):
		cpu+=1
		print("cpu's choice",a)
		print("yourscore:",yourscore)
		print("cpu:",cpu)
	elif(a=="scissors" and b=="stone"):
		yourscore+=1
		print("cpu's choice",a)
		print("yourscore:",yourscore)
		print("cpu:",cpu)
	else:
		print("both are same")
		print("yourscore:",yourscore)
		print("cpu:",cpu)
if(cpu>yourscore):
	print("cpu is the winner")
elif(cpu==yourscore):
	print("match ended in a draw")
else:
	print("you're the winner")		
