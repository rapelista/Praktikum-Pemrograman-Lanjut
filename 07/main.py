def check(ori, edit):
    if ori == edit:
        print("Palindrom")
    else:
        print("Bukan palindrom")


# BUAT Reverse Kata
def reverse(word):
    kata_reverse = word[::-1]
    check(word, kata_reverse)


n = int(input("Jumlah kata: "))
for i in range(n):
    kata = input("Masukkan kata: ")
    reverse(kata)
