from typing import List

print('\nTYPE DATA SKALAR =>TYPE DATA SEDERHANA')  #TYPE DATA SKALAR => TYPE DATA SEDERHANA
kucing1 = 'Jika'
kucing2 = 'Juwi'
kucing3 = 'Jutri'
kucing4 = 'Juca'

print(kucing1)
print(kucing2)
print(kucing3)
print(kucing4)

print('\nType Data List(Daftar) atau array')  # Type Data List(Daftar) atau array
kucing = [' Jika', 'Juwi', 'Jutri', 'Juca']
print(kucing)
kucing.append('Jontor') #append menyisipkan perintah
print(kucing)

print('\nsapa kucing ke-2')   #Menyapa kucing ke 2
print(f'Hai {kucing[3]}!')

print('\nsapa semua kucing') #Sapa Semua anak
for n_k in kucing:
    print(f'Hai {n_k}!')

print('\nSapa semua anak cara ribet')
for n_k in range(0, len(kucing)):       #len fungsi di python utk mengambil list
    #print(f'Hai kucing comel {kucing [n_k]}')      #f merupakan definisikan variable
    print(f'{n_k+1}. Hai kucing {kucing [n_k]}')      #f merupakan definisikan variable




