# Funkcije, ki generirajo izpis za igralca

import model

def izpis_poraza(igra):
    return 'Porabili ste preveč poskusov. Pravilno geslo je {}.'.format(igra.geslo)

def izpis_zmage(igra):
    return 'Uspešno ste uganili geslo {}.'.format(igra.geslo)

def izpis_igre(igra):
    tekst = (
        '==============================\n\n'
        '   {trenutno_stanje}'
        'Neuspesni poskusi: {poskusi}\n\n'
        '=============================='
    ).format(trenutno_stanje=igra.pravilni_del_gesla(), poskusi=igra.nepravilni_ugibi())

    return tekst

#Izvajanje vmesnika

def zahtevaj_vnos():
    vnos = input('Poskusi uganiti črko: ')
    return vnos

def preveri_vnos(vnos):
    '''Funkcija vrne True , če je vnos primeren, sicer igralca opozori in vrne Fale'''
    if len(vnos) != 1:
        print('Neveljaven vnos! Vnesi zgolj eno črko.')
        return False
    else:
        return True

def zazeni_vmesnik():
    igra = model.nova_igra()

    while True:
        # Izpišemo stanje
        print(izpis_igre(igra))
        # Igralec ugiba
        poskus = zahtevaj_vnos()  # !!! Še ni napisano
        if not preveri_vnos(poskus):
            continue    # Preskoči preostanek zanke


        rezultat = igra.ugibaj(poskus)
        # Preverimo, če je igre konec
        if igra.poraz():       #  ali pa napišemo:   if rezultat == model.PORAZ:
            print(izpis_poraza)
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return

zazeni_vmesnik()