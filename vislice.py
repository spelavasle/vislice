import bottle, model
SKRIVNI_KLJUC = 'Skoraj je že konec tedna!'

vislice = model.Vislice('stanje.json')

# Igra je namenjena testiranju
#id_testne_igre = vislice.nova_igra()
#(testna_igra, poskus) = vislice.igre[id_testne_igre]

# Dodajmo teste v testno igro
#vislice.ugibaj(id_testne_igre, 'A')
#vislice.ugibaj(id_testne_igre, 'B')
#vislice.ugibaj(id_testne_igre, 'C')

@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')

#@bottle.post('/igra/')
#def prikaz_testne_igre():
#    return bottle.template('igra.tpl', igra=testna_igra)

@bottle.post('/nova_igra/')
def zacni_novo_igro():
    # Naredi novo igro
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre',id_igre, secret=SKRIVNI_KLJUC, path='/')
    # Preusmeri na naslov za igranje nove igre
    bottle.redirect('/igra/')
    return 
    
@bottle.get('/igra/')
def prikazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, poskus) = vislice.igre[id_igre]
    
    return bottle.template('igra.tpl', 
                            igra=igra, 
                            id_igre=id_igre, 
                            poskus=poskus)

@bottle.post('/igra/')
def ugibaj_crko():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    crka = bottle.request.forms.getunicode('poskus')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')

bottle.run(debug=True, reloder=True)