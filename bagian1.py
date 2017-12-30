def menyimpan_data(nama,tinggi,berat):
	file=open("berat.txt","a+")
	data=file.write("Nama Anda %s \n"%(nama))
	data=file.write("Tinggi Anda %i \n"%(tinggi))
	data=file.write("Berat Badan Anda %i \n"%(berat))
	
def berat_ideal():
	ideal = (tinggi-100)-(tinggi-100)*15/100
	file=open("berat.txt","a+")
	data=file.write("Berat Badan Ideal Anda adalah %i\n"%(ideal))
	return ideal
	
def makanan():
	makanan=("Apel","Kacang Almond","Blueberry","Bayam","Kacang Merah","Brokoli","Pisang")
	return makanan
	
def olahraga():
	olahraga={1:"Lari",2:"Push Up",3:"Berenang",4:"Pull Upp",5:"Sit Up"}
	return olahraga
	
def option():
	print("Pilihlah Salah Satu dari Lima Fungsionalitas dibawah Ini: ")
	print("1. Menyimpan Data")
	print("2. Berat Badan Ideal")
	print("3. Makanan yang dianjurkan")
	print("4. Olahraga yang dianjurkan")
	print("5. Keluar Program")
	pilihan=int(input("Masukan pilihan Anda: "))
	return pilihan
	
#main program
pilihan= True
while(pilihan<5):
	pilihan= option()
	if (pilihan==5): 
		break;
	if(pilihan==1): 
		nama= str(input("Masukan Nama: "))
		tinggi= int(input("Masukan Tinggi: "))
		berat= int(input("Masukan Berat: "))
		menyimpan_data(nama,tinggi,berat)
		print("-------- Menyimpan Data ---------\n")
	if(pilihan==2):
		b = berat_ideal()
		print("Berat Badan Ideal %i"%(b))
		if(berat<b):
			print("Anda Kekurangan Berat Badan")
		elif(berat>b):
			print("Anda Kelebihan Berat Badan")
		print("---------------------------------\n")
	if(pilihan==3): 
		m= makanan()
		print("Makan makanan berikut untuk menjaga berat badan Anda: ", (m))
		print("-------------------------------------------\n")
	elif(pilihan==4):
		o= olahraga()
		print("Olahraga yang dianjurkan adalah: ", (o))
		print("--------------------------------------\n")