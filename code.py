Nama = input('Nama :')
Obat = input('Jenis Obat :')
Jumlah = int(input('Jumlah Obat :'))
Uang = int(input('Berapa Uang Anda :'))
data_obat = ['paracetamol', 'antibiotik', 'pereda nyeri', 'obat batuk']
harga = 10000
if Obat not in data_obat:
    Hasil = 'Mohon Maaf, Obat yang Anda Cari Tidak Tersedia'
else:
    Total = Jumlah * harga
    Kembalian = Uang - Total
    Hasil = (f'Nama: {Nama}, Obat: {Obat}, Jumlah Obat: {Jumlah}, Total: {Total}, Kembalian: {Kembalian}')
print(Hasil)