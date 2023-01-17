class Ojek():
    
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
    
    def cek_id_abang(self):
        print('nama :',self.nama,'\nmotor :',self.transmisi,'\ndaerah :',self.daerah)
        
ojek1 = Ojek('mario', 'manual', 'tangerang')
ojek2 = Ojek('Asep', 'Automatic', 'tangerang kota')

ojek1.cek_id_abang()
ojek2.cek_id_abang()