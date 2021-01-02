"""
Type data dict sekedar menghubungkan antara key $ value
KVP=Key Value Pair
dictionarey=kamus
type data dict dimulai dengan{} dan di cetak lebih lengkap antara key dan hasilnya
"""

kamus_ind_lon = {
    'anak': 'son',
    'istri': 'wife',
    'bapak': 'father',
    'kakek': 'opa'
}  # data yang d baca 1 arah

print(kamus_ind_lon)
print(kamus_ind_lon['bapak'])  # value
print(kamus_ind_lon['kakek'])
print(kamus_ind_lon['istri'])

print('\nData ini di kirimkan oleh serv gojek utk pemakai aps')

data_dari_server_gojek = {
    'tanggal': '2020-12-9',
    'driver_list': [
        {'nama': 'Jika', 'jarak': 10},
        {'nama': 'Juwi', 'jarak': 30},
        {'nama': 'Jutri', 'jarak': 50},
        {'nama': 'Juca', 'jarak': 70},
        {'nama': 'Jontor', 'jarak': 90}
    ]
} #Kurawal menandakan variable

print('\ndata_dari_server_gojek')

print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver_list']}")

print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #2 {data_dari_server_gojek['driver_list'][1]}")
print(f"Driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver #5 {data_dari_server_gojek['driver_list'][4]}")

print(f"\njarak driver #1 {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
print(f"jarak driver #2 {data_dari_server_gojek['driver_list'][1]['jarak']} meter")
print(f"jarak driver #3 {data_dari_server_gojek['driver_list'][2]['jarak']} meter")
print(f"jarak driver #4 {data_dari_server_gojek['driver_list'][3]['jarak']} meter")
print(f"jarak driver #5 {data_dari_server_gojek['driver_list'][4]['jarak']} meter")

