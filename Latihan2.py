import datetime

# Definisikan kelas untuk hotel
class Hotel:
    def __init__(self, nama, harga, ketersediaan):
        self.nama = nama
        self.harga = harga
        self.ketersediaan = ketersediaan

    # Fungsi untuk menampilkan detail hotel
    def tampilkan_detail(self):
        print(f"Nama Hotel: {self.nama}")
        print(f"Harga: Rp{self.harga}/malam")
        print(f"Ketersediaan Kamar: {self.ketersediaan} kamar")

# Definisikan daftar hotel yang tersedia
daftar_hotel = [
    Hotel("OYO", 200.000, 5),
    Hotel("Bobobox", 400.000, 3),
    Hotel("Grand Mercure", 500.000, 2)
]

# Fungsi untuk menampilkan daftar hotel
def tampilkan_hotel():
    print("Daftar Hotel yang Tersedia:")
    for index, hotel in enumerate(daftar_hotel):
        print(f"{index+1}. {hotel.nama}")

# Fungsi untuk memilih hotel dan jumlah malam inap
def pesan_hotel():
    while True:
        tampilkan_hotel()
        pilihan_hotel = int(input("Pilih nomor hotel yang ingin dipesan: "))
        if pilihan_hotel < 1 or pilihan_hotel > len(daftar_hotel):
            print("Nomor hotel tidak valid. Silakan coba lagi.\n")
            continue
        malam_inap = int(input("Berapa malam ingin menginap: "))
        break

    # Menghitung tanggal check-in dan check-out
    check_in = datetime.date.today()
    check_out = check_in + datetime.timedelta(days=malam_inap)

    # Menghitung harga total
    hotel_terpilih = daftar_hotel[pilihan_hotel-1]
    harga_total = hotel_terpilih.harga * malam_inap

    # Memperbarui ketersediaan hotel
    hotel_terpilih.ketersediaan -= 1

    # Menampilkan konfirmasi pesanan
    print("\n==============================")
    print("        Konfirmasi Pesanan")
    print("==============================")
    print(f"Nama Hotel: {hotel_terpilih.nama}")
    print(f"Check-in: {check_in.strftime('%d %B %Y')}")
    print(f"Check-out: {check_out.strftime('%d %B %Y')}")
    print(f"Durasi Inap: {malam_inap} malam")
    print(f"Harga: Rp{hotel_terpilih.harga}/malam")
    print(f"Total Harga: Rp{harga_total}")
    print("==============================")

# Memulai program
while True:
    pesan_hotel()
    lanjutkan = input("Apakah anda ingin memesan hotel lagi? (ya/tidak): ")
    if lanjutkan.lower() == "n":
        break
