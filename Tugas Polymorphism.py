class Ikan:
    def intro(self):
        print("Di dunia ini ada beberapa type yang berbeda dari spesies ikan")
    
    def insang(self):
        print("Hampir semua ikan bernafas dengan insang, namun ada beberapa ikan yang tidak bernafas dengan insang")

class Hiu(Ikan):
    def insang(self):
        print("Hiu bernapas dengan insang")

class Paus(Ikan):
    def insang(self):
        print("Paus tidak bernapas dengan insang")

obj_ikan = Ikan()
obj_hiu = Hiu()
obj_paus = Paus()

obj_ikan.intro()
obj_ikan.insang()

obj_hiu.intro()
obj_hiu.insang()

obj_paus.intro()
obj_paus.insang()