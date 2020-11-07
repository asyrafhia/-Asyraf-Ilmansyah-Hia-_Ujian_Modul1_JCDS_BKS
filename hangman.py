
import random

i = random.randint(0,2)
clue = ['Pemain Bola', 'Hewan seperi Zebra', 'Minuman Bayi']
jawaban = ['Mohammed Salah', 'kuda', 'susu']
print(clue)
kata_kunci = jawaban[i]
kata_tebak = []
panjang_kakun = len(kata_kunci)

for i in kata_kunci:
    kata_tebak.append('_')


print(f'Kata yang perlu ditebak berjumlah {panjang_kakun} huruf: {"".join(kata_tebak)}')
print('Masukkan 1 huruf di setiap attempt dan kesempatan salah huruf hanya 7x saja')

kesempatan = 1
salah = 0

class salah_angka():
    def __init__(self):
        self.salah_satu = '_____'
        self.salah_dua = '_____\n|   |\n|   O'
        self.salah_tiga = '_____\n|   |\n|   O\n|  /|\ \n'
        self.salah_empat = '_____\n|   |\n|   O\n|  /|\ \n|  / \ \n'
        self.salah_lima = '_____\n|   |\n|   O\n|  /|\ \n|  / \ \n'
        self.salah_enam = '_____\n|   |\n|   O\n|  /|\ \n|  / \ \n'
        self.cukup = 'None'

gambar = salah_angka()

while (kesempatan):
    var = input(f'attempt {kesempatan}: ')
    if var in kata_kunci:
        if len(var) > 1:
            print('Hanya bisa diinput satu huruf saja')
        elif len(var) == 1:
            for i in range(0,panjang_kakun):
                if kata_kunci[i] == var:
                    kata_tebak[i] = var
            print(''.join(kata_tebak))
            
            if '_' not in kata_tebak:
                print('You won!')
                break

    else:
        if len(var) > 1:
            print('Hanya bisa diinput satu huruf saja')
        elif len(var) == 1:
            salah += 1
            if (salah == 1):
                # print('HANG')
                print(gambar.salah_satu)
            elif (salah == 2):
                # print('HANGMAN')
                print(gambar.salah_dua)
            elif (salah == 3):
                # print('HANGMAN')
                print(gambar.salah_tiga)
            elif (salah == 4):
                # print('HANGMAN')
                print(gambar.salah_empat)
            elif (salah == 5):
                # print('HANGMAN')
                print(gambar.salah_lima)
            else:
                # print('HANGMAN')
                print(gambar.salah_enam)
                print('HANGMAN!: YOU ARE DEAD')
                break

    kesempatan += 1