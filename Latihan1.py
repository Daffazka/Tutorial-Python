import datetime

# Definisikan kelas untuk hotel
class Hotel:
    def __init__(self, nama, harga, ketersediaan):
        self.nama = nama
        self.harga = harga
        self.ketersediaan = ketersediaan

# Definisikan daftar hotel yang tersedia
daftar_hotel = [
    Hotel("Grand Mercure Hotel", 200000, 6),
    Hotel("Oyo", 300000, 4),
    Hotel("Ibis Style Hotel", 400000, 3)
]

# Fungsi untuk menampilkan daftar hotel
def tampilkan_hotel():
    print("Daftar Hotel yang Tersedia:")
    for index, hotel in enumerate(daftar_hotel):
        print(f"{index+1}. {hotel.nama} - Rp{hotel.harga}/malam")

# Fungsi untuk memilih hotel dan jumlah malam inap
def pesan_hotel():
    tampilkan_hotel()
    pilihan_hotel = int(input("Pilih nomor hotel yang ingin dipesan: "))
    malam_inap = int(input("Berapa malam ingin menginap: "))

    # Menghitung tanggal check-in dan check-out
    check_in = datetime.date.today()
    check_out = check_in + datetime.timedelta(days=malam_inap)

    # Menghitung harga total
    hotel_terpilih = daftar_hotel[pilihan_hotel-1]
    harga_total = hotel_terpilih.harga * malam_inap

    # Memperbarui ketersediaan hotel
    hotel_terpilih.ketersediaan -= 1

    # Menampilkan konfirmasi pesanan
    print(f"\nPesanan anda untuk menginap di {hotel_terpilih.nama} selama {malam_inap} malam dari {check_in.strftime('%d %B %Y')} hingga {check_out.strftime('%d %B %Y')} dengan total harga Rp{harga_total} telah diterima.")

# Memulai program
pesan_hotel()
