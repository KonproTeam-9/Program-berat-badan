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
	
def option():
	print("Pilihlah Salah Satu dari Lima Fungsionalitas dibawah Ini: ")
	print("1. Menyimpan Data")
	print("2. Berat Badan Ideal")
	pilihan=int(input("Masukan pilihan Anda: "))
	return pilihan
	
#main program
pilihan= True
while(pilihan<5):
	pilihan= option()
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
		break;