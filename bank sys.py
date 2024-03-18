import random
import time
import markdown
from tqdm import tqdm
import csv
pr = " WELOCOME TO BANK OF BARODA"
print(pr.center(60))
print("1. make account ")
print("2. check balance")
print("3. deposit money")
print("4. withdraw money")
print("5. check fd returns")
print("6. transfer money")
print("7. Take loan")
print("8. close account")
print("9. show account details")
print("10. Exit and Save your account details")
print("11. customer care")
class Bank :
	def __init__(self,nam,c,n,l,fd) :
		self.name=nam
		self.id=c
		self.owner = n
		self.deposit = l
		self.fd = fd
	def display(self) :
		print("your total balance is",self.deposit)
	def depositss(self,depos) :
		self.deposit = self.deposit + depos
		print("deposit succesfull")
	def withdraws(self,withs) :
		self.deposit = self.deposit-withs
		print("withdraw succesfull")
	def fds(self,year) :
		print("your total amount of deposited is now",self.fd)
		vars = 0
		fdam = (self.fd*7*1)/100
		while(vars<year) :
			time.sleep(1)
			vars += 1
			self.fd = fdam + self.fd
			print(f"your total amount of fixed deposit of {vars} year is",self.fd)
	def loan(self) :
		url = "https://www.bankofbaroda.in"
		mark = markdown.markdown(url)
		print(mark)
		print("visit this above link and apply for your loan ")
		print("and check your eligibility")
		print("thank you so much")
	def show(self) :
		print(f"account holder name : {self.name}")
		print(f"account id : {self.id}")
		print(f"number of owners : {self.owner}")
		print(f"account balance : {self.deposit}")
		print(f"fixed deposit amount :{self.fd}")
pes = []	
o = []
list = []
kio = False
def loadbar() :
	total_it = 100
	print("wait while proccesing")
	for i in tqdm(range(total_it)) :
			time.sleep(0.01)
	print("money transfer successfull")
while True :
	prin = "if your not old user then press'N"
	print(prin)
	prins = "THANK YOU SO MUCH"
	print(prins)
	user = input("do u have an account ??")
	if(user=='Y') :
		print("1. deposit money (once)")
		print("2. withdraw money (once)")
		print("3. display details (once)")
		print("4. Apply for loan (once)")
		print("5. Transfer money (once)")
		with open('md.csv',mode = 'r') as fold :
			read = csv.reader(fold)
			for row in read :
				list.append(row)
	#	print(list)
		whe = int(input("what do u want to do ? "))
		if(whe==1) :
				ide = input("enter your account name")
				moun = int(input("enter amount"))
				for i,  rows in enumerate(list):
					if ide in rows :
						rows[3] = int(rows[3]) + moun
						list[i]= rows
						with open("md.csv" , mode = "w",newline= "") as fol :
							write = csv.writer(fol)
							write.writerows(list)
						print("deposit succesful")
		if(whe==2) :
				ide = input("enter your account name")
				moun=int(input("how much money u want to withdraw ?"))
				for i, rows in enumerate(list) :
					if ide in rows :
						if(int(rows[3])>=moun) :
							rows[3] = int(rows[3]) - moun
							list[i] = rows
							with open("md.csv" , mode = 'w' , newline="") as fol :
								write = csv.writer(fol)
								write.writerows(list)
							print("withdraw succesful")	
						else :
							print("your account does not have sufficient baalnce")
		if(whe==3) :
				ide = input("enter your account name")
				kel = []
				for i , rows in enumerate(list) :
					if ide in rows :
						kel.append(rows)
				if kel==[] :
					print("there is no such account that exist in this bank , if you does not have any account than make it ")
				else :
					print(kel)
		if(whe==4) :
					ide = input("enter your account name")
					uno = input("is that your savings account")
					loa = input("do u really wanna take loan then press 'Y' for yes")
					if(loa == 'Y' and uno == 'Y') :
						url = "https://www.bankofbaroda.in"
						mark = markdown.markdown(url)
						print(mark)
						print("visit this above link and apply for ur loan")
						print("thank u")
					else :
						print("this is not your savings account you cant take loan on this account")
		if(whe==5) :
				print("you only transfer money once ")
				print("To transfer money again then rerun the programm thank you")
				ide = input("enter your account name")
				foe = input("enter the account name where you want to transfer")
				mount = int(input("how much money u want to transfer"))
				for i , rows in enumerate(list) :
					if ide in rows  :
						if(int(rows[3])>mount) :
							kio = True
							rows[3] = int(rows[3]) - mount
							list[i] = rows
							with open("md.csv", mode = 'w') as fold :
								write = csv.writer(fold)
								write.writerows(list)
						elif(int(rows[3])<mount) :
							print("your account does not have sufficient balance")
							break
				for j,cols in enumerate(list) :
					if foe in cols :
						cols[3] = int(cols[3]) + mount
						list[j] = cols
						with open ("md.csv",mode= 'w') as fold :
							write = csv.writer(fold)
							write.writerows(list)
				if(kio == True) :
					loadbar()
						
		
			
		
	else :
		a = int(input("what do u want to do?"))
		if(a==1) :
			savi = input("press 'S' for savings account and 'F' for fixed deposit")
			if (savi == 'S') :
				kes = []
				print("Enter your details properly")
				nam = input("enter your name")
				c = random.randint(1000000,9999999)
				print(c,"remember this id for your future works")
				pan= input("enter your pan details")
				d = input("want to do joint account press 'Y' for yes ")
				if (d=="Y") :
					n = int(input("how many owners ?"))
					for i in range(n) :
						g = input("enter names")
				else :
					n = 1
				l = int(input("deposit minimum 1000 ruppes for savings account"))
				fd = 0
				year = 0
			if(savi=='F') :
				kes = []
				k = input("want to do fixed deposit press 'Y' for yes")
				if (k=="Y") :
					print("Enter your details properly")
					nam = input("enter your name")
					n = 1
					c = random.randint(1000000,9999999)
					print(c,"remember this id for your future works")
					pan= input("enter your pan details")
					l = 0
					fd = int(input("deposit minimum amount of 10k"))
					year = int(input("how many years ?"))
					print("This bank give 7 percent interest on fixed deposit yearly")
			kes.append(nam)
			kes.append(c)
			kes.append(n)
			kes.append(l)
			kes.append(fd)
			pes.append(kes)		
			o.append(Bank(nam,c,n,l,fd))
			print("you make ur account succesfully to save your account press 10")
		if (a==2 and o!=[]) :
			ids = int(input("enter your account id"))
			if(o==[]) :
				print("there is no account")
			else :
				for j in o :
					if (j.id==ids) :
						j.display()
						kio = True
				if kio == False :
					print("There is no such account that exist")
		if (a==3 and o!=[]) :
			ids = int(input("enter your account id properly"))
			if(o==[]) :
				pass
			else :
				for j in o :
					if(j.id==ids) :
						depos=int(input("how much money u want to deposit ?"))
						j.depositss(depos)
						j.display()
						kio = True
				if(kio==False) :
					print("there is no such account that exist")
		if (a==4) :
			ids = int(input("enter your account id properly"))
			if (o==[]) :
				print("there is no such account ")
			else :
				for j in o :
					if(j.id==ids) :
						withs = int(input("how much money you want to withdraw?"))
						j.withdraws(withs)	
						j.display()
						kio = True
				if(kio==False) :
					print("there is no such account that exist")
		if(a ==5 and o!=[]) :
				ids = int(input("enter your account id properly"))
				if(o==[]) :
					pass
				else :
					for j in o :
						if(j.id==ids) :
							kio = True
							j.fds(year)
					if(kio==False) :
						print("there is no such account that exist")
		if(a==6 and o!=[]) :
				ids = int(input("enter your account id properly"))
				for j in o :
					if(j.id==ids) :
						ide = int(input("enter the account id where u want to transfer your money"))
						namer = input("enter the account holder name")
						kio = True
					
						for z in o :
							if(z.id==ide and z.name == namer and kio== True) :
								amount = int(input("how much amount you want to send ??"))
								total_it = 100
								print("wait while proccesing")
								for i in tqdm(range(total_it)) :
									time.sleep(0.1)
								z.depositss(amount)
								j.withdraws(amount)
					if(kio==False) :
						print("there is no such account")
		if(a == 7 and o!=[]) :
				ids = int(input("enter your account id properly"))
				loaner = input("want to take loan ?")
				for j in o :
						if(j.id==ids and loaner == 'Y') :
							kio = True 
							if(savi=='S') :
								j.loan()
							else :
								print("you cant take loan on your fd account .. if you want to take loan make a savings account and apply for a loan")
								print("thank you so much")
				if(kio==False):
					print("there is no such account")			
		if(a==8) :
				rem = input("want to close ur existing bank account ??")
				if(rem =="Y") :
							ids = int(input("enter the acc id which u want to close"))
							for j in o :
								if(j.id == ids) :
									print(f"do you really want to close {j.name} account?")
									real = input()
									if(real =="Y") :
										del j 
		if(a==9 and o!=[]) :
				ids = int(input("enter your account id"))
				for j in o :
					if(j.id==ids) :
						kio = True
						j.show()
				if(kio==False) :
					print("there is no such account that exist")
		if(a==10) :
			break 	
		if(a==11) :
			url = "rudraparbat714@gmail.com"
			print(url)
			print("contact through this mail for further querry ")	
			
								
with open("md.csv" ,mode = 'a' ) as file :
					write= csv.writer(file)
					for rows in pes :
							write.writerow(rows)
					print("your account details saved succesfully")
							
print("THANK YOU VISIT AGAIN".center(60))			
					
		
		
		
			
	
