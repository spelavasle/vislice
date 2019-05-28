import random
import json

# Definirajmo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

# Definiramo logični model igre

class Igra:
    
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper()  # string    (tipi, ki jih bomo uporabli)
        self.crke = crke  #list
        return 

    def napacne_crke(self):
        seznam_napacnih_crk = []
        for x in self.crke:
            if x not in self.geslo:
                seznam_napacnih_crk.append(x) 
        return seznam_napacnih_crk   
        
    def pravilne_crke(self):
        seznam_pravilnih_crk = []
        for x in self.crke:
            if x in self.geslo:
                seznam_pravilnih_crk.append(x) 
        return seznam_pravilnih_crk 

    #def pravilne_crke(self):
    #    return [c for c in self.crke if c in self.geslo()]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    #def stevilo_napak(self):
    #   return len()self.napacne_crke())
    
    def zmaga(self):
       # if self.poraz():
       #    return False
            for crka in self.geslo:
                if crka not in self.crke:
                    return False
            return True

    def poraz(self):
        return self.stevilo_napak() > 10
  
    #def poraz(self):
    #    return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
        
    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += ' ' + crka
            else:
                niz +=' _'
        niz = niz.strip()     # počistimo presledke, ki smo jih nardili gor
        return niz

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            return NAPACNA_CRKA

# Izluščimo vse slovenske besede
bazen_besed = []

with open("besede.txt", 'r', encoding='utf-8') as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)

# Funkcije za generiranj iger

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


class Vislice:

    def __init__(self, datoteka_s_stanjem):
        # V slovarju igre ima vsaka igra svoj ID
        # ID je celo število
        self.igre = {} 
        self.datoteka_s_stanjem = datoteka_s_stanjem
        return 

#    def prost_id_igre(self):
#        if self.igre == {}:
#            return 0
#        else:
#            # Preverimo katero od prvih 'n+1' števil še ni uporabljeno za id 'n'm iger.
#            for i in range(len(self.igre) + 1)
#                if i not in self.igre.keys():
#                    return i

# Ali pa isto funkcijo zapišemo:
    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1 


    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        # (Naredi novo igro z naključnim geslom)
        # Ustvar novo igro in nov ID
        igra = nova_igra()
        nov_id = self.prost_id_igre()

        # (Shrani (igra, ZACETEK) v slovar z novim ID)
        # Dodaj v slovar iger
        self.igre[nov_id] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return nov_id


    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        # Pridobi igro
        (igra, _) = self.igre[id_igre]
        # Ugibaj
        nov_poskus = igra.ugibaj(crka)
        # Shrani rezultat poskusa v slovar
        self.igre[id_igre] = (igra, nov_poskus)
        self.zapisi_igre_v_datoteko()
        return 

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as datoteka:
            zakodirane_igre = json.load(datoteka)  #dobimo slovar z (geslo, crke)
            igre = {}
            for id_igre in zakodirane_igre:
                igra = zakodirane_igre[id_igre]
                igre[int(id_igre)]= (Igra(igra['geslo'], igra['crke']), igra['poskus'])
            self.igre = igre
        return

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w') as datoteka:
            zakodirane_igre = {}
            for id_igre in self.igre:
                (igra, poskus) = self.igre[id_igre]
                zakodirane_igre[id_igre] = {'geslo': igra.geslo, 'crke': igra.crke, 'poskus': poskus}
            json.dump(zakodirane_igre, datoteka)
        return