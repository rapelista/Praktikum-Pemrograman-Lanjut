# ambil data dari user.csv

# ketika hak akses == 1

# ganti isi file hello.txt pakai mode "w"
if hak_akses == 1:
    with open("hello.txt", "w") as file:
        file.write("diganti sama apa")
