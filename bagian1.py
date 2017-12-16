def menyimpan_data(nama,tinggi,berat):
	file=open("berat.txt","a+")
	data=file.write("Nama Anda %s \n"%(nama))
	data=file.write("Tinggi Anda %i \n"%(tinggi))
	data=file.write("Berat Badan Anda %i \n"%(berat))
	
def option():
	print("Pilihlah Salah Satu dari Lima Fungsionalitas dibawah Ini: ")
	print("1. Menyimpan Data")
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
		break;