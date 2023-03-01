def kata_terpanjang(sentence):
    work = sentence.split()
    hasil = ''
    for word in work:
        if len(word) > len(hasil):
            hasil= word
    return hasil

aaaaa = input("Masukkan sebuah kalimat: ")
wwww_word = kata_terpanjang(aaaaa)
print("Kata terpanjang dalam kalimat adalah:", wwww_word)