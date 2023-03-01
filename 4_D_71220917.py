nomor = input("Masukkan sekumpulan bilangan (pisahkan dengan spasi): ")
screet = list(map(int, nomor.split(",")))


besar_nomor = lambda aaa: max(aaa)
print("bilangan terbesar dari kumpulan bilangan yang di input adalah", besar_nomor(screet))


kecil_num = lambda bbb: min(bbb)
print("bilangan terkecil dari kumpulan bilangan di input adalah ", kecil_num(screet))