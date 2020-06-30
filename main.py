# basic python construction
# sequential
print('hello world!')
print('by Arin')
print('30 June 2020')
print('_' * 5)

#percabangan: Eksekusi terpilih
ingin_cepat = True
if ingin_cepat:
    print('jalan terus aja ya!')
else:
    print('pilih jalan lain')

#Perulangan
jumlah_anak = 4

for index_anak in range(1,jumlah_anak+1):
    print(f'Halo anak {index_anak}!')