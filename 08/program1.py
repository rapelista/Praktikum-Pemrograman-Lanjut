class Orang:
    total = 0

    def __init__(self, nama):
        self.nama = nama
        Orang.total += 1

    def __del__(self):
        Orang.total -= 1

    def katakanHalo(self):
        print('Halo, nama saya %s, apa kabar?' % self.nama)

    def total_populasi(self):
        print('Total Orang %s' % self.total)

    total_populasi = classmethod(total_populasi)


org = Orang('Budi')
org.katakanHalo()
org.total_populasi()
org2 = Orang('Andi')
org2.katakanHalo()
org.total_populasi()
print('obyek dihapus')
del org
del org2
Orang.total_populasi()
