# KONSTRUKSI DASAR PYTHON

# SEQUENTIAL_(KODE LURUS) : exekusi berurutan
print('hello world')
print('by rachmat')
print('tanggal 26 des 2020')
print('-' * 20)

# PERCABANGAN: Exekuesi Terpilih
ingin_cepat= True
if ingin_cepat:
    print('\njalan lurus ya..')
else:
    print('jalan lain')

#PERULANGAN
jumlah_kucing = 5
for index_k in range(1, jumlah_kucing + 1): #jumlah perulangan = 5-1=4
    print(f'kucing jelek #{index_k}')
