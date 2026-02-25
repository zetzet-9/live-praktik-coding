import colorama
from colorama import Fore, Back, Style
import time

try:
    colorama.init()
except Exception as e:
    print(f"Error initializing colorama: {e}")
    exit(1)

def cerita():
    print(Fore.YELLOW + Style.BRIGHT + "🏰 PETUALANGAN ANAK BUDAK DI KEKAISARAN 🏰" + Style.RESET_ALL)
    print("\n" + "="*60 + "\n")

    # Pendahuluan
    print(Fore.CYAN + "Di sebuah kekaisaran yang megah, ada seorang anak laki-laki berusia 10 tahun bernama Alex." + Style.RESET_ALL)
    print(Fore.CYAN + "Ia adalah seorang budak yang berhasil melarikan diri dari pasar jual-beli budak. 🏃‍♂️" + Style.RESET_ALL)
    print(Fore.CYAN + "Sekarang, ia mencari orangtua kandungnya yang hilang. 😢" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Rintangan 1: Direndahkan oleh bangsawan
    print("\n" + Fore.RED + "🚧 RINTANGAN PERTAMA: Direndahkan oleh Bangsawan 🚧" + Style.RESET_ALL)
    print(Fore.WHITE + "Alex berjalan di jalanan kota, tapi seorang bangsawan melihatnya dan merendahkannya." + Style.RESET_ALL)
    print(Fore.WHITE + "'Hei, budak kotor! Pergi dari sini!' kata bangsawan sambil tertawa. 🤣" + Style.RESET_ALL)
    print(Fore.WHITE + "Apa yang akan Alex lakukan?" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Jawab dengan sopan dan pergi" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Diam saja dan terus berjalan" + Style.RESET_ALL)
    pilihan = input("Pilih opsi (1/2): ")
    if pilihan == "1":
        print(Fore.WHITE + "Alex menjawab sopan: 'Maaf, Tuan.' dan pergi. 😔" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Alex diam saja dan terus berjalan. 😶" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Rintangan 2: Dipukuli
    print("\n" + Fore.RED + "🚧 RINTANGAN KEDUA: Dipukuli karena Menganggu 🚧" + Style.RESET_ALL)
    print(Fore.WHITE + "Di pasar, Alex tidak sengaja menabrak seorang bangsawan lain." + Style.RESET_ALL)
    print(Fore.WHITE + "Bangsawan itu marah dan memukulinya. 👊💥" + Style.RESET_ALL)
    print(Fore.WHITE + "Apa yang akan Alex lakukan?" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Minta maaf dan lari" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Lawan kembali" + Style.RESET_ALL)
    pilihan = input("Pilih opsi (1/2): ")
    if pilihan == "1":
        print(Fore.WHITE + "Alex minta maaf dan lari cepat. 🏃‍♂️" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Alex mencoba lawan, tapi kalah dan tetap lari. 😵" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Rintangan 3: Mencari cara keluar wilayah
    print("\n" + Fore.RED + "🚧 RINTANGAN KETIGA: Meninggalkan Wilayah dengan Kereta Kuda 🚧" + Style.RESET_ALL)
    print(Fore.WHITE + "Alex perlu meninggalkan wilayah ini. Ia melihat kereta kuda yang akan berangkat." + Style.RESET_ALL)
    print(Fore.WHITE + "Tapi ia tidak punya uang. Ia harus menyelinap naik kereta. 🐎🚂" + Style.RESET_ALL)
    print(Fore.WHITE + "Apa yang akan Alex lakukan?" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Tunggu sampai gelap dan naik" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Cari pekerjaan kecil untuk uang" + Style.RESET_ALL)
    pilihan = input("Pilih opsi (1/2): ")
    if pilihan == "1":
        print(Fore.WHITE + "Alex menunggu gelap dan berhasil naik kereta. ✅" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Alex bekerja sebentar, dapat uang, dan naik kereta resmi. 💰" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Rintangan tambahan 1: Lapar
    print("\n" + Fore.RED + "🚧 RINTANGAN TAMBAHAN: Lapar dan Haus 🚧" + Style.RESET_ALL)
    print(Fore.WHITE + "Di perjalanan, Alex sangat lapar. Ia mencari makanan di hutan. 🍎" + Style.RESET_ALL)
    print(Fore.WHITE + "Ia menemukan buah-buahan liar, tapi harus hati-hati dengan binatang buas. 🐺" + Style.RESET_ALL)
    print(Fore.WHITE + "Apa yang akan Alex lakukan?" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Ambil buah dan lari" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Cari tempat aman dulu" + Style.RESET_ALL)
    pilihan = input("Pilih opsi (1/2): ")
    if pilihan == "1":
        print(Fore.WHITE + "Alex ambil buah dan lari dari binatang. 🏃‍♂️🍎" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Alex cari tempat aman, lalu ambil buah. 🛡️" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Rintangan tambahan 2: Cuaca buruk
    print("\n" + Fore.RED + "🚧 RINTANGAN TAMBAHAN: Hujan Deras 🚧" + Style.RESET_ALL)
    print(Fore.WHITE + "Tiba-tiba hujan deras turun. Alex basah kuyup dan kedinginan. 🌧️❄️" + Style.RESET_ALL)
    print(Fore.WHITE + "Ia mencari tempat berteduh di bawah pohon besar. 🌳" + Style.RESET_ALL)
    print(Fore.WHITE + "Apa yang akan Alex lakukan?" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Tetap di bawah pohon" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Cari gua atau rumah terdekat" + Style.RESET_ALL)
    pilihan = input("Pilih opsi (1/2): ")
    if pilihan == "1":
        print(Fore.WHITE + "Alex tetap di bawah pohon sampai hujan reda. 🌳" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Alex cari gua dan berteduh di sana. 🕳️" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Rintangan tambahan 3: Pencuri
    print("\n" + Fore.RED + "🚧 RINTANGAN TAMBAHAN: Diserang Pencuri 🚧" + Style.RESET_ALL)
    print(Fore.WHITE + "Di malam hari, sekelompok pencuri mendekati Alex. 🦹‍♂️" + Style.RESET_ALL)
    print(Fore.WHITE + "Mereka ingin merampoknya. Apa yang akan Alex lakukan?" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Lari cepat" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Sembunyi dan tunggu" + Style.RESET_ALL)
    pilihan = input("Pilih opsi (1/2): ")
    if pilihan == "1":
        print(Fore.WHITE + "Alex lari cepat dan lolos. 🏃‍♂️" + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Alex sembunyi dan pencuri pergi. 🔍" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Masuk wilayah kekaisaran
    print("\n" + Fore.GREEN + "🌟 MASUK KE WILAYAH KEKAISARAN 🌟" + Style.RESET_ALL)
    print(Fore.WHITE + "Setelah melewati banyak rintangan, Alex tiba di wilayah kekaisaran utama. 🏰" + Style.RESET_ALL)
    print(Fore.WHITE + "Orang-orang di jalan menatapnya dengan heran. 👀" + Style.RESET_ALL)
    print(Fore.WHITE + "'Dia sangat mirip dengan Kaisar!' bisik mereka. 🤔👑" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Ditemukan pengawal
    print("\n" + Fore.BLUE + "🛡️ DITEMUKAN PENGAWAL 🛡️" + Style.RESET_ALL)
    print(Fore.WHITE + "Seorang pengawal istana melihat Alex dan mengenalinya. 🛡️" + Style.RESET_ALL)
    print(Fore.WHITE + "'Kau mirip Kaisar! Ikut aku ke istana.' kata pengawal. 🚶‍♂️🏰" + Style.RESET_ALL)
    print(Fore.WHITE + "Alex dibawa ke istana dengan kereta kuda. 🐎🚂" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Di istana
    print("\n" + Fore.MAGENTA + "🏰 DI ISTANA KAISAR 🏰" + Style.RESET_ALL)
    print(Fore.WHITE + "Di istana, Kaisar melihat Alex. 👑" + Style.RESET_ALL)
    print(Fore.WHITE + "Istri Kaisar, sang Ratu, tidak senang. 😠👸" + Style.RESET_ALL)
    print(Fore.WHITE + "'Siapa anak ini? Ia mungkin bahaya!' kata Ratu. ⚠️" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Tuduhan Ratu
    print("\n" + Fore.RED + "🚨 TUDUHAN RATU 🚨" + Style.RESET_ALL)
    print(Fore.WHITE + "Ratu menentang dan menuduh Alex sebagai suruhan musuh. 🦹‍♀️" + Style.RESET_ALL)
    print(Fore.WHITE + "'Ia ingin menghancurkan kekaisaran!' kata Ratu. 💥🏰" + Style.RESET_ALL)
    print(Fore.WHITE + "Ratu mengusulkan tes DNA dengan Kaisar. 🧬" + Style.RESET_ALL)
    print(Fore.WHITE + "Kaisar setuju. ✅" + Style.RESET_ALL)
    input("\nTekan Enter untuk melanjutkan...")

    # Hasil tes
    print("\n" + Fore.YELLOW + "🧬 HASIL TES DNA 🧬" + Style.RESET_ALL)
    print(Fore.WHITE + "Tes DNA menunjukkan Alex adalah anak Kaisar. 👨‍👦" + Style.RESET_ALL)
    print(Fore.WHITE + "Tapi Kaisar terkejut melihat tanda lahir di tangan Alex. 🤯✋" + Style.RESET_ALL)
    print(Fore.WHITE + "'Tanda lahir ini... sama seperti ibumu!' kata Kaisar. 😲" + Style.RESET_ALL)
    print(Fore.WHITE + "Kaisar bertanya: 'Siapa ibumu?' 🤔" + Style.RESET_ALL)
    print(Fore.WHITE + "Apa yang akan Alex jawab?" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Saya tidak tahu" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Ibu saya bernama Oddete, dan ini kalung peninggalannya" + Style.RESET_ALL)
    print(Fore.GREEN + "3. (Langsung) Tes DNA positif, Alex diangkat menjadi Putra Mahkota" + Style.RESET_ALL)
    while True:
        pilihan = input("Pilih opsi (1/2/3): ")
        if pilihan in ["1", "2", "3"]:
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Pilih 1, 2, atau 3." + Style.RESET_ALL)
    if pilihan == "1":
        print("\n" + Fore.MAGENTA + "🔍 PENEMUAN BESAR 🔍" + Style.RESET_ALL)
        print(Fore.WHITE + "Alex menjawab: 'Saya tidak tahu, Tuan.' 😢" + Style.RESET_ALL)
        print(Fore.WHITE + "Kaisar berkata: 'Ibunya adalah bangsawan tercinta yang meninggal dalam perang 10 tahun lalu. Jasadnya tidak pernah ditemukan.' 💔" + Style.RESET_ALL)
        print(Fore.WHITE + "Kaisar sangat mencintainya. ❤️" + Style.RESET_ALL)
        print(Fore.WHITE + "Alex diangkat menjadi Putra Mahkota! 👑👦" + Style.RESET_ALL)
    elif pilihan == "2":
        print("\n" + Fore.MAGENTA + "🔍 PENEMUAN BESAR 🔍" + Style.RESET_ALL)
        print(Fore.WHITE + "Alex menjawab: 'Ibu saya bernama Oddete.' dan memberi kalung peninggalannya. 📿" + Style.RESET_ALL)
        print(Fore.WHITE + "Kaisar terkejut: 'Kalung ini... aku yang memberikannya pada ibumu!' 😲" + Style.RESET_ALL)
        print(Fore.WHITE + "Kaisar berkata: 'Odette.. istriku.' 💔" + Style.RESET_ALL)
        print(Fore.WHITE + "Ibunya adalah bangsawan tercinta yang meninggal dalam perang 10 tahun lalu. Jasadnya tidak pernah ditemukan. 💔" + Style.RESET_ALL)
        print(Fore.WHITE + "Kaisar sangat mencintainya. ❤️" + Style.RESET_ALL)
        print(Fore.WHITE + "Alex diangkat menjadi Putra Mahkota! 👑👦" + Style.RESET_ALL)
    else:
        print("\n" + Fore.MAGENTA + "🔍 PENEMUAN BESAR 🔍" + Style.RESET_ALL)
        print(Fore.WHITE + "Tes DNA menunjukkan hasil positif! Alex adalah anak Kaisar. 🧬✅" + Style.RESET_ALL)
        print(Fore.WHITE + "Alex diangkat menjadi Putra Mahkota! 👑👦" + Style.RESET_ALL)
    input("\nTekan Enter untuk mengakhiri...")

    # Akhir
    print("\n" + Fore.GREEN + Style.BRIGHT + "🎉 AKHIR CERITA 🎉" + Style.RESET_ALL)
    print(Fore.WHITE + "Alex hidup bahagia sebagai pangeran di kekaisaran. 🏰😊" + Style.RESET_ALL)
    print(Fore.YELLOW + "Dari hari itu, Alex belajar tentang kekuasaan, kebijaksanaan, dan cinta. 🌟" + Style.RESET_ALL)
    print(Fore.CYAN + "Ia menjadi pemimpin yang adil, mengingat perjalanannya dari budak menjadi pangeran. 👑" + Style.RESET_ALL)
    print(Fore.MAGENTA + "Petualangan ini mengajarkan bahwa takdir bisa berubah, dan keluarga selalu ada. ❤️" + Style.RESET_ALL)

if __name__ == "__main__":
    cerita()
