import random


def playerMilih(prompt):
    while True:
        try:
            print(prompt)
            pilihan = int(input("Silahkan pilih nomor pilihan Anda: "))
            if not 0 < pilihan < 4:
                print("Tolong pilih nomor yang telah disediakan")
            else:
                return pilihan
        except ValueError:
            print("Tolong Masukkan Angka!\n")


def computerMilih():
    return random.randrange(1, 4)


def cek(player, computer):
    if player == 1 and computer == 2:
        hasil = 2
    elif player == 1 and computer == 3:
        hasil = 1
    elif player == 2 and computer == 1:
        hasil = 1
    elif player == 2 and computer == 3:
        hasil = 2
    elif player == 3 and computer == 1:
        hasil = 2
    elif player == 3 and computer == 2:
        hasil = 1
    else:
        hasil = 0
    return hasil


def keguba():
    pilihan = ["Kertas", "Gunting", "Batu"]
    menangPlayer = 0
    menangComputer = 0
    print(
        "\n--- Selamat datang di permainan Kertas-Gunting-Batu ---\nAturan Main:\n- Kertas kalah oleh Gunting\n- Gunting kalah oleh Batu\n- Batu kalah oleh Kertas"
    )
    while True:
        try:
            berapaKali = int(input("Berapa kali Anda ingin bermain (Masukan Angka): "))
            break
        except ValueError:
            print("Tolong jangan memasukkan huruf!\n")

    for x in range(berapaKali):
        pilihanPlayer = playerMilih(
            f"\nPertandingan Ke-{x + 1}\nPilihan:\n1. Kertas\n2. Gunting\n3. Batu"
        )
        pilihanComputer = computerMilih()
        print(
            f"\nPlayer: {pilihan[pilihanPlayer - 1]} Vs Computer: {pilihan[pilihanComputer - 1]}"
        )
        match cek(pilihanPlayer, pilihanComputer):
            case 0:
                pass
            case 1:
                menangPlayer += 1
            case 2:
                menangComputer += 1
    print()
    if menangPlayer == menangComputer:
        print("Hasilnya adalah seri!!!")
    elif menangPlayer > menangComputer:
        print("Selamat Anda memenangkan permainan ini!!!")
    else:
        print("Anda kalah")
    print()


def suit():
    print(
        "\n--- Selamat datang di permainan Kertas-Gunting-Batu ---\nAturan Main:\n- Kertas kalah oleh Gunting\n- Gunting kalah oleh Batu\n- Batu kalah oleh Kertas"
    )
    print("Pilihan:\n1. Kertas\n2. Gunting\n3. Batu")


def main():
    print("=== Selamat Datang di proyek 1 saya!! ===")
    while True:
        match input(
            "Menu:\n1. Kertas-Gunting-Batu\n2. Suit\n3. Keluar Program\nSilahkan pilih nomor menu: "
        ):
            case "1":
                keguba()
            case "2":
                suit()
            case "3":
                break
            case _:
                print("Pilih nomor menu yang telah disediakan!!!\n")


if __name__ == "__main__":
    main()
