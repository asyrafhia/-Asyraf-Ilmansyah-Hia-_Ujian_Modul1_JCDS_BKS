def sort_odd_even(num):
    print(f'Angka Awal: {num}')
    index_of_num = []
    index_ganjil = []
    angka_ganjil = []
    index_genap = []
    angka_genap = []
    gabung = [' ' for i in range(len(num))]
    
    # for i in num:
    #     index_ganjil.append(num.index(i))

    for x, y in enumerate(num):
        index_of_num.append(x)
        if y%2 == 1:
            index_ganjil.append(x)
            angka_ganjil.append(y)
        else:
            index_genap.append(x)
            angka_genap.append(y)

    # print(index_ganjil)
    # print(angka_ganjil)
    # print(index_genap)
    # print(angka_genap)
    
    angka_ganjil.sort(reverse=False)  # sort keci ke besar
    # print(angka_ganjil)

    angka_genap.sort(reverse=True)  # sort besar ke kecil
    # print(angka_genap)

    # Hasil Angka Ganjil
    hasil = [' ' for i in range(len(num))]
    for x, y in zip(index_ganjil,angka_ganjil):
        hasil[x] = y
    print(f'Hasil Sortir Angka Ganjil dari Terkecil sampai Terbesar Sesuai Index Awalnya: {hasil}')
    # print(''.join(map(str,hasil)))

    for j in index_ganjil:
        gabung[j] = hasil[j]
    # print(gabung)

    # Hasil Angka Genap
    hasil = [' ' for i in range(len(num))]
    for x, y in zip(index_genap,angka_genap):
        hasil[x] = y
    print(f'Hasil Sortir Angka Genap dari Terbesar sampai Terkecil Sesuai Index Awalnya: {hasil}')
    # print(''.join(map(str,hasil)))

    for j in index_genap:
        gabung[j] = hasil[j]
    # print(f'Hasil Gabungan Angka Ganjil dan Genap Sesuai Index: {gabung}')
    return f'Hasil Gabungan Angka Ganjil dan Genap Sesuai Index Awal: {gabung}'

# sort_odd_even([5,3,2,8,1,4])
print(sort_odd_even([5,3,2,8,1,4]))
