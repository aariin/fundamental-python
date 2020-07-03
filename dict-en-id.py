"""
dicitonary data type connect between key and value
kamus itu satu arah, jadi misal mau cari bahasa indonesia nya ya bikin lagi
"""

dict_ID_EN = {'anak': 'kid', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(dict_ID_EN)
print(dict_ID_EN['anak'])

print('\nData ini dikirimkan oleh server Gojek untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-07-01',
    'driver_list': [{'nama': 'Nina', 'jarak': 100}, {'Alex'}, {'Laura'}, {'Onky'}]
}
print(data_dari_server_gojek)
print(f"driver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
